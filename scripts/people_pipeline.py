"""
This is the main script to pull job data from RapidAPI and store it in MongoDB.
"""

import sys
import os
import logging
import warnings
import pandas as pd
import streamlit as st
import requests
import time
from retry import retry

warnings.filterwarnings("ignore")

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Local imports
from config.singleton import Singleton
from scripts.insert_data_in_db import InsertData
from scripts.helper_functions import HelperFunctions
from scripts.rapid_api import RapidAPI
from scripts.mongo_client import MongoDBClient


logger = logging.getLogger(__name__)


class PeopleFetcherPipeline:
    def __init__(self, mongo_client, status=None):
        self.client = mongo_client
        self.raw_collection = self.client.get_collection("RawPeople")
        self.clean_collection = self.client.get_collection("People")
        self.helper = HelperFunctions()
        self.inserter = InsertData()
        self.status = status or st.status(
            "👥 Fetching people pipeline...", expanded=True
        )

    def fetch_recruiters(self, jobs_df: pd.DataFrame) -> pd.DataFrame:
        recruiter_records = []
        for _, row in jobs_df.iterrows():
            job_id = row.get("job_id")
            job_url = row.get("job_url")
            company_name = row.get("company_name")
            try:
                response = RapidAPI().get_hiring_team(job_id, job_url)
                items = response.get("data", {}).get("items", [])
                if items:
                    for item in items:
                        item.update(
                            {
                                "job_id": job_id,
                                "job_url": job_url,
                                "company_name": company_name,
                            }
                        )
                        recruiter_records.append(item)
            except Exception as e:
                logger.warning(f"Error fetching recruiters for job_id {job_id}: {e}")

        self.status.write(f"👥 Total Hiring Managers found : {len(recruiter_records)}")
        return pd.DataFrame(recruiter_records)

    def fetch_people_by_company(self, company: str, search_keywords: list) -> list:
        results = []
        for keyword in search_keywords:
            try:
                response = RapidAPI().search_people(keywords=keyword, company=company)
                items = response.get("data", {}).get("items", [])
                for item in items:
                    item["company_name"] = company
                results.extend(items)
                if len(results) >= 5:
                    break
            except Exception as e:
                logger.info(
                    f"Failed fetching people for {company}, keyword {keyword}: {e}"
                )
        return results

    def collect_people_data(self, recruiter_df, final_jobs_df):
        if not recruiter_df.empty:
            recruiter_job_ids = set(recruiter_df["job_id"].dropna())
        else:
            recruiter_job_ids = set()

        all_job_ids = set(final_jobs_df["job_id"].dropna())
        remaining_jobs = final_jobs_df[
            final_jobs_df["job_id"].isin(all_job_ids - recruiter_job_ids)
        ]

        if remaining_jobs.empty:
            return pd.DataFrame()

        self.status.write("👥 Finding prospects for jobs without recruiters...")
        search_keywords = [
            "Human Resource, HR, Talent Acquisition, IT Recruiter, Founder",
        ]  # "CTO, Chief Technology Officer, COO, CXO, VP, Vice President, Co-Founder, CEO, MD, Director",
        companies = remaining_jobs["company_name"].dropna().unique()
        people_data = [
            person
            for company in companies
            for person in self.fetch_people_by_company(company, search_keywords)
        ]
        return pd.DataFrame(people_data)

    @retry(tries=5, delay=2, backoff=2)
    def fetch_profile(self, link):
        try:
            existing = list(
                self.raw_collection.find(
                    {"profileURL": link},
                    {"_id": 0, "message_date": 0, "company_name": 0},
                )
            )
            if existing:
                return existing[0]

            response = RapidAPI().get_linkedin_profile_data_by_url(link)
            if isinstance(response, requests.Response) and response.status_code == 429:
                raise requests.exceptions.HTTPError("429 Too Many Requests")
            if response:
                response["profileURL"] = link
            return response
        except requests.exceptions.HTTPError as e:
            if "429" in str(e):
                logger.warning(f"Rate limit hit for {link}. Retrying...")
                raise
            logger.warning(f"HTTPError for {link}: {e}")
        except Exception as e:
            logger.warning(f"Error fetching profile for {link}: {e}")
        return {}

    def enrich_profiles(self, people_df: pd.DataFrame) -> pd.DataFrame:
        self.status.write("📄 Fetching LinkedIn profiles...")
        profiles = []
        for link in people_df["profileURL"].dropna().unique():
            profiles.append(self.fetch_profile(link))
            time.sleep(2)
        profiles_df = pd.DataFrame(profiles)
        profiles_df = pd.merge(
            profiles_df,
            people_df[["profileURL", "company_name"]],
            on="profileURL",
            how="right",
        )
        return profiles_df

    def process_profiles(self, profiles_df):
        selected = [
            "id",
            "profileURL",
            "company_name",
            "username",
            "firstName",
            "lastName",
            "headline",
            "geo",
            "educations",
            "position",
            "fullPositions",
            "skills",
            "summary",
            "volunteering",
        ]
        final = profiles_df[
            [col for col in selected if col in profiles_df.columns]
        ].copy()
        final["processed_fullPositions"] = (
            final["fullPositions"].dropna().apply(self.helper.process_full_positions)
        )
        final["latest_experience"] = final.apply(
            lambda row: self.helper.find_relevant_experience(
                row["processed_fullPositions"], None
            ),
            axis=1,
        )
        final = pd.concat(
            [
                final.drop(columns=["latest_experience", "geo"], errors="ignore"),
                pd.json_normalize(final["latest_experience"]),
                pd.json_normalize(final["geo"]),
            ],
            axis=1,
        )
        final["clean_skills"] = final["skills"].apply(self.helper.process_skills)
        final.rename(
            columns={"company_name": "company", "full": "full_address"}, inplace=True
        )
        drop_cols = [
            "start.year",
            "start.month",
            "start.day",
            "end.year",
            "end.month",
            "end.day",
            "educations",
            "position",
            "fullPositions",
            "skills",
            "volunteering",
            "id",
            "country",
            "city",
            "countryCode",
        ]
        final.drop(
            columns=[col for col in drop_cols if col in final.columns], inplace=True
        )
        return final

    def run(self, final_jobs_df):
        self.status.write("👥 Starting Prospect data pipeline...")
        recruiter_df = self.fetch_recruiters(final_jobs_df)
        recruiter_df.rename(columns={"url": "profileURL"}, inplace=True)

        people_df = self.collect_people_data(recruiter_df, final_jobs_df)
        final_people_df = pd.concat([people_df, recruiter_df], ignore_index=True)

        profiles_df = self.enrich_profiles(final_people_df)
        self.inserter.insert_or_upsert_to_mongo(
            self.client, "RawPeople", self.inserter.prepare_data(profiles_df)
        )

        final_people = self.process_profiles(profiles_df)
        self.inserter.insert_or_upsert_to_mongo(
            self.client, "People", self.inserter.prepare_data(final_people)
        )

        self.status.write(f"✅ Total prospects found: {len(final_people)}")
        return final_people

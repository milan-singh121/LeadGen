"""
This is the main script to pull job data from RapidAPI and store it in MongoDB.
"""

import sys
import os
import logging
import warnings
import pandas as pd
import streamlit as st
from pymongo import MongoClient

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


class JobFetcherPipeline:
    def __init__(self, mongo_client: MongoDBClient, status=None):
        self.client = mongo_client
        self.db_raw = self.client.get_collection("RawJobs")
        self.db_clean = self.client.get_collection("Jobs")
        self.helper = HelperFunctions()
        self.inserter = InsertData()
        self.status = status

    def log_progress(self, message):
        if self.status:
            self.status.write(message)
        else:
            print(message)

    def fetch_jobs(self, keywords, **filters):
        if isinstance(keywords, str):
            keyword_list = [k.strip() for k in keywords.split(",") if k.strip()]
        elif isinstance(keywords, list):
            keyword_list = [str(k).strip() for k in keywords if str(k).strip()]
        else:
            raise ValueError("keywords must be a string or list of strings")

        all_jobs = []
        for kw in keyword_list:
            try:
                response = RapidAPI().search_jobs(keywords=kw, **filters)
                jobs = response.get("data", [])
                self.log_progress(f"✅ {len(jobs)} jobs fetched for keyword '{kw}'")
                all_jobs.extend(jobs)
            except Exception as e:
                self.log_progress(f"⚠️ Error fetching jobs for '{kw}': {e}")
        return all_jobs

    def clean_and_filter_jobs(self, jobs_raw):
        jobs_df = pd.DataFrame([self.helper.flatten_dict(job) for job in jobs_raw])
        if jobs_df.empty:
            return pd.DataFrame()

        jobs_df.rename(columns={"id": "job_id"}, inplace=True)
        clean_jobs = jobs_df.dropna(subset=["company_url"]).reset_index(drop=True)
        clean_jobs["company_username"] = clean_jobs["company_url"].str.extract(
            r"/company/([^/]+)/"
        )
        clean_jobs["linkedinUrl"] = clean_jobs["company_url"].str.replace(
            r"/life$", "", regex=True
        )
        return clean_jobs

    def get_existing_job_ids(self):
        cursor = self.db_raw.find({}, {"_id": 0, "job_id": 1})
        return {doc["job_id"] for doc in cursor if "job_id" in doc and doc["job_id"]}

    def _insert_jobs(self, collection_name, df):
        if df.empty:
            return
        prepared_data = self.inserter.prepare_data(df)
        self.inserter.insert_or_upsert_to_mongo(
            self.client, collection_name, prepared_data
        )

    def run(self, keywords, **filters):
        self.log_progress("🔍 Fetching jobs from RapidAPI...")
        jobs_raw = self.fetch_jobs(keywords, **filters)

        if not jobs_raw:
            self.log_progress("❌ No jobs fetched.")
            return pd.DataFrame()

        clean_jobs = self.clean_and_filter_jobs(jobs_raw)
        if clean_jobs.empty:
            self.log_progress("❌ No jobs with valid company URLs.")
            return pd.DataFrame()

        new_job_ids = set(clean_jobs["job_id"].dropna().unique())
        existing_job_ids = self.get_existing_job_ids()
        actual_new_job_ids = new_job_ids - existing_job_ids

        main_jobs_df = clean_jobs[
            clean_jobs["job_id"].isin(actual_new_job_ids)
        ].reset_index(drop=True)

        if main_jobs_df.empty:
            self.log_progress("⚠️ No new jobs to process.")
            return pd.DataFrame()

        self.log_progress(f"📦 Total new jobs to insert: {len(main_jobs_df)}")

        self._insert_jobs("RawJobs", main_jobs_df)

        jobs_to_clean = main_jobs_df.copy()
        jobs_to_clean.drop(
            columns=[
                col
                for col in [
                    "referenceId",
                    "posterId",
                    "company_logo",
                    "postedTimestamp",
                ]
                if col in jobs_to_clean
            ],
            inplace=True,
        )
        jobs_to_clean.rename(columns={"url": "job_url"}, inplace=True)
        self._insert_jobs("Jobs", jobs_to_clean)

        return jobs_to_clean

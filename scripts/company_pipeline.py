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


logger = logging.getLogger(__name__)


class CompanyFetcherPipeline:
    def __init__(self, mongo_client, status=None):
        self.client = mongo_client
        self.raw_collection = self.client.get_collection("RawCompany")
        self.clean_collection = self.client.get_collection("Company")
        self.helper = HelperFunctions()
        self.inserter = InsertData()
        self.status = status

    def log_progress(self, message):
        if self.status:
            self.status.write(message)
        else:
            print(message)

    def fetch_existing_companies(self):
        existing_docs = list(self.raw_collection.find({}, {"_id": 0}))
        return pd.DataFrame(existing_docs)

    def find_missing_companies(self, jobs_df, existing_df):
        if jobs_df.empty:
            return pd.DataFrame(), pd.DataFrame()

        new_urls = set(jobs_df["linkedinUrl"].dropna().unique())
        existing_urls = set(existing_df["linkedinUrl"].dropna().unique())

        present = new_urls & existing_urls
        missing = new_urls - existing_urls

        already_present = existing_df[
            existing_df["linkedinUrl"].isin(present)
        ].reset_index(drop=True)
        not_present = jobs_df[jobs_df["linkedinUrl"].isin(missing)].reset_index(
            drop=True
        )
        return already_present, not_present

    def fetch_company_data(self, usernames):
        results = []
        for username in usernames:
            try:
                data = RapidAPI().get_linkedin_company_details_by_username(username)
                results.append(data.get("data", {}))
            except Exception as e:
                self.log_progress(f"❌ Error fetching company '{username}': {e}")
        if results:
            return pd.DataFrame(results).dropna(how="all").reset_index(drop=True)
        else:
            return pd.DataFrame()  # safer than returning None

    def parse_staff_range(self, range_str):
        try:
            if "+" in range_str:
                return pd.Series([0, int(range_str.replace("+", ""))])
            lower, upper = map(int, range_str.split("-"))
            return pd.Series([lower, upper])
        except Exception:
            return pd.Series([None, None])

    def clean_company_data(self, df):
        drop_cols = [
            "Images",
            "isClaimable",
            "backgroundCoverImages",
            "logos",
            "callToAction",
            "followerCount",
            "featuredCustomers",
            "pageVerification",
        ]
        df.drop(columns=drop_cols, inplace=True, errors="ignore")

        if "founded" in df:
            founded_df = pd.json_normalize(df["founded"])
            df.drop(columns=["founded"], inplace=True)
            df = df.join(founded_df.rename(columns={"year": "founded_year"}))

        if "staffCountRange" in df:
            df[["lower_limit", "upper_limit"]] = df["staffCountRange"].apply(
                self.parse_staff_range
            )
        return df

    def run(self, jobs_df):
        self.log_progress("🚀 Starting company data pipeline...")

        # Step 1: Fetch from DB
        existing_df = self.fetch_existing_companies()

        # Step 2: Find missing vs present
        already_present, not_present = self.find_missing_companies(jobs_df, existing_df)

        # Step 3: Fetch new company data
        if not not_present.empty:
            usernames = not_present["company_username"].dropna().unique()
            new_company_df = self.fetch_company_data(usernames)

            if new_company_df is not None and not new_company_df.empty:
                new_company_df.rename(columns={"id": "companyId"}, inplace=True)
                full_df = pd.concat(
                    [already_present, new_company_df], ignore_index=True
                )
            else:
                full_df = already_present.copy()
        else:
            full_df = already_present.copy()

        # Step 4: Merge and insert into RawCompany
        if not full_df.empty:
            self.inserter.insert_or_upsert_to_mongo(
                self.client, "RawCompany", self.inserter.prepare_data(full_df)
            )

            # Step 5: Clean for final company DB
            full_df_cleaned = self.clean_company_data(full_df)

            if not full_df_cleaned.empty:
                # Step 6: Filter ICP-fit companies
                icp_fit = (
                    full_df_cleaned[full_df_cleaned["upper_limit"] <= 200]
                    .copy()
                    .reset_index(drop=True)
                )

                if not icp_fit.empty:
                    # Step 7: Insert into production company collection
                    self.inserter.insert_or_upsert_to_mongo(
                        self.client, "Company", self.inserter.prepare_data(icp_fit)
                    )

                    self.log_progress(f"🏁 {len(icp_fit)} ICP-fit companies inserted.")
                    return icp_fit

        self.log_progress("⚠️ No valid companies to insert.")
        return None

"""
This is the main script to pull data from Rapid A
"""

import sys
import os
import logging
import warnings
import pandas as pd
from retry import retry
import streamlit as st
import requests
import time
from time import sleep
from random import uniform

warnings.filterwarnings("ignore")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.singleton import Singleton
from scripts.insert_data_in_db import InsertData
from scripts.helper_functions import HelperFunctions
from scripts.rapid_api import RapidAPI
from scripts.jobs_pipeline import JobFetcherPipeline
from scripts.company_pipeline import CompanyFetcherPipeline
from scripts.people_pipeline import PeopleFetcherPipeline
from scripts.posts_pipeline import PostsFetcherPipeline


logger = logging.getLogger(__name__)


class Orchestrator:
    """
    This is the main class which will execute step by step to pull data from Rapid API
    """

    @staticmethod
    def run_job(
        client,
        keywords,
        location,
        date_posted,
        job_type,
        function_id,
        industry_id,
        onsite_remote,
        sort,
        status=None,
    ):
        status = status or st.status(
            "🚀 Running lead generation pipeline...", expanded=True
        )

        def run_job_and_company_pipeline():
            # Fetch Jobs based on Filter Criteria
            jobs_pipeline = JobFetcherPipeline(mongo_client=client, status=status)
            job_filters = {
                "location": location,
                "date_posted": date_posted,
                "job_type": job_type,
                "function_id": function_id,
                "industry_id": industry_id,
                "onsite_remote": onsite_remote,
                "sort": sort,
            }
            jobs_df = jobs_pipeline.run(keywords=keywords, **job_filters)

            if jobs_df is None:
                return None, None

            # Fetch Comapny Details
            company_pipeline = CompanyFetcherPipeline(
                mongo_client=client, status=status
            )
            company_df = company_pipeline.run(jobs_df)

            return jobs_df, company_df

        # Initial run
        jobs_df, company_df = run_job_and_company_pipeline()

        if jobs_df is None:
            st.warning(
                "⚠️ No new jobs found for the given filters. Please try again with different filter combinations."
            )
            st.stop()

        # Loop until 15+ unique companies or 3 total attempts
        counter = 1
        max_attempts = 3
        min_companies_required = 50

        while (
            company_df is not None
            and not company_df.empty
            and company_df["linkedinUrl"].nunique() < min_companies_required
            and counter < max_attempts
        ):
            status.write(
                f"⚠️ Only {company_df['linkedinUrl'].nunique()} unique companies found after {counter} attempts."
            )

            new_jobs_df, new_company_df = run_job_and_company_pipeline()

            if new_company_df is not None and not new_company_df.empty:
                company_df = (
                    pd.concat([company_df, new_company_df], ignore_index=True)
                    .drop_duplicates(subset="linkedinUrl", keep="first")
                    .reset_index(drop=True)
                )

            if new_jobs_df is not None and not new_jobs_df.empty:
                jobs_df = (
                    pd.concat([jobs_df, new_jobs_df], ignore_index=True)
                    .drop_duplicates(subset="job_id", keep="first")
                    .reset_index(drop=True)
                )

            counter += 1

        if company_df is not None and not company_df.empty:
            status.write(
                f"🏁 Company pipeline completed: {len(company_df)} ICP-fit companies found."
            )
        else:
            st.warning(
                "⚠️ No ICP company found. Please try again with different filter combinations."
            )
            st.stop()

        # Combine Jobs and Company to get the final list of companies that meet the criteria
        if jobs_df is None or company_df is None:
            status.write("❌ Unable to merge jobs and companies.")
            return (
                pd.DataFrame(),
                pd.DataFrame(),
                pd.DataFrame(),
                pd.DataFrame(),
                pd.DataFrame(),
            )

        final_jobs = pd.merge(jobs_df, company_df, on="linkedinUrl", how="right")

        # Find People from the company
        people_pipeline = PeopleFetcherPipeline(mongo_client=client, status=status)
        people_df = people_pipeline.run(final_jobs)

        # Fetch LinkedIn posts of the people
        posts_pipeline = PostsFetcherPipeline(mongo_client=client, status=status)
        posts_df = posts_pipeline.run(people_df)

        status.write("✅ Data fetched and stored successfully.")

        return jobs_df, company_df, people_df, posts_df, final_jobs

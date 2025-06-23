"""
This script contains the main code for the complete workflow.
"""

import sys
import os
import logging
import pandas as pd
import warnings
import streamlit as st

warnings.filterwarnings("ignore")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.singleton import Singleton
from scripts.mongo_client import MongoDBClient
from scripts.helper_functions import HelperFunctions
from scripts.job_openings import JobOpenings
from scripts.email_finder import SnovEmailFinder
from scripts.email_sequence import GetEmailSequence
from scripts.snov_data_dump import Snov
from scripts.insert_data_in_db import InsertData

logger = logging.getLogger(__name__)


class LeadGen(metaclass=Singleton):
    """
    This class contains the main code for the complete workflow.
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def run_email_sequence_pipeline(
        keywords,
        location,
        date_posted,
        job_type,
        function_id,
        industry_id,
        onsite_remote,
        sort,
    ) -> pd.DataFrame:
        """
        Streamlit-compatible version of the lead generation pipeline.
        """

        status = st.status("🚀 Running lead generation pipeline...", expanded=True)

        with status:
            st.write("📡 Connecting to MongoDB...")
            client = MongoDBClient()

            st.write("🔍 Fetching job openings and people data...")
            jobs_df, final_people, posts_df, company_df = (
                JobOpenings().get_job_openings(
                    client,
                    keywords,
                    location,
                    date_posted,
                    job_type,
                    function_id,
                    industry_id,
                    onsite_remote,
                    sort,
                    status=status,
                )
            )

            st.write("📥 Collecting emails from LinkedIn URLs...")
            email_from_url_data = SnovEmailFinder().collect_emails_from_linkedin_urls(
                final_people
            )

            st.write("📩 Enriching missing emails...")
            emails_data = SnovEmailFinder().enrich_missing_emails(email_from_url_data)

            st.write("🔗 Merging email data with people...")
            final_people = (
                pd.merge(
                    final_people,
                    emails_data[
                        [
                            "profileURL",
                            "name",
                            "emails",
                            "currentJob_position",
                            "currentJob_site",
                            "domain",
                        ]
                    ],
                    on="profileURL",
                    how="left",
                )
                .drop_duplicates(subset=["profileURL"])
                .reset_index(drop=True)
            )

            st.write("🧠 Generating questionnaire summaries...")
            questionnaire_response = HelperFunctions().get_questionnaire_data(
                jobs_df, company_df, final_people, posts_df
            )

            st.write("✉️ Generating email sequences...")
            all_emails = GetEmailSequence().generate_email_sequence(
                final_people, jobs_df, posts_df
            )
            all_emails = all_emails.dropna().reset_index(drop=True)

            st.write("🧽 Formatting email output...")
            final_emails = GetEmailSequence().format_emails(all_emails)

            st.write("🧹 Cleaning bullet points in emails...")
            email_body_cols = [f"Email Body {i}" for i in range(1, 6)]
            for col in email_body_cols:
                if col in final_emails.columns:
                    final_emails[col] = final_emails[col].apply(
                        GetEmailSequence().remove_line_breaks
                    )

                    # final_emails[col] = (
                    #     final_emails[col]
                    #     .astype(str)
                    #     .apply(HelperFunctions().fix_bullet_breaks)
                    # )
                    # final_emails[col] = (
                    #     final_emails[col]
                    #     .astype(str)
                    #     .apply(HelperFunctions().fix_numbered_bullet_breaks)
                    # )

            st.write("🧬 Merging all data...")
            final_people = pd.merge(
                final_people,
                questionnaire_response,
                left_on="company",
                right_on="Company Name",
                how="left",
            ).drop(columns="Company Name")

            final_data = pd.merge(
                final_people,
                final_emails,
                left_on="profileURL",
                right_on="LinkedIn URL",
                how="left",
            ).drop(columns=["First Name", "Last Name", "LinkedIn URL"])

            final_data = final_data.drop_duplicates(subset=["profileURL"]).reset_index(
                drop=True
            )

            st.write("📧 Handling fallback emails for missing values...")
            final_data.loc[final_data["emails"].isna(), "emails"] = (
                final_data["firstName"] + "@yopmail.com"
            )

            st.write("📤 Dumping data into Snov.io...")
            Snov().dump_data_in_snov(final_data)

            st.write("📤 Dumping data into MongoDB...")

            final_data = HelperFunctions().format_final_data(final_data)
            inserter = InsertData()
            inserter.insert_or_upsert_to_mongo(
                client, "FinalData", inserter.prepare_data(final_data)
            )

            status.update(label="✅ Pipeline completed!", state="complete")

        return final_data

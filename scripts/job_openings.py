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


logger = logging.getLogger(__name__)


class JobOpenings(metaclass=Singleton):
    """
    This class contains the main function "get_job_opening" which
    pulls the jobs and continues to rest of the process.
    """

    @staticmethod
    def select_rows_from_dataframe(
        df: pd.DataFrame,
        key_columns: list,
        display_title: str = "✅ Review and Select Rows to Proceed",
        session_key: str = "selected_rows",
        checkbox_label: str = "✅ Keep?",
        form_key: str = "selection_form",
        checkbox_help: str = "Check to include in next steps",
    ) -> pd.DataFrame:
        """
        Reusable function to display a dataframe with checkbox selection,
        confirm selection via a form, and persist across reruns using session state.
        """
        selected_flag_key = f"{session_key}_confirmed"

        # Step 0: Init session state
        st.write("🔄 Initializing session state keys...")
        if session_key not in st.session_state:
            st.session_state[session_key] = None
        if selected_flag_key not in st.session_state:
            st.session_state[selected_flag_key] = False

        st.markdown(f"### {display_title}")

        # Step 1: Column check
        st.write("🧪 Checking required columns...")
        if not all(k in df.columns for k in key_columns):
            missing = [k for k in key_columns if k not in df.columns]
            st.warning(f"Missing columns: {', '.join(missing)}. Cannot proceed.")
            st.stop()

        # Step 2: Add checkbox column if missing
        if "select" not in df.columns:
            st.write("➕ Adding 'select' column...")
            df["select"] = False
        else:
            st.write("✅ 'select' column already exists.")

        # Step 3: Show form if not yet confirmed
        if not st.session_state[selected_flag_key]:
            st.info(
                f"Please select the rows you wish to proceed with by checking the '{checkbox_label}' box."
            )
            st.write("📋 Displaying selection form...")
            with st.form(form_key, clear_on_submit=False):
                editable_df = st.data_editor(
                    df[["select"] + key_columns],
                    use_container_width=True,
                    num_rows="dynamic",
                    column_config={
                        "select": st.column_config.CheckboxColumn(
                            checkbox_label, help=checkbox_help, default=False
                        )
                    },
                    hide_index=True,
                    key=f"editor_{form_key}",
                )

                submitted = st.form_submit_button("✅ Confirm Selection and Continue")

                st.write(f"📥 Form submitted: {submitted}")
                if submitted:
                    selected_df = editable_df[editable_df["select"] == True].copy()
                    st.write(f"🟢 Selected rows: {len(selected_df)}")

                    if selected_df.empty:
                        st.warning(
                            "⚠️ No rows selected. Please select at least one to proceed."
                        )
                    else:
                        st.session_state[session_key] = selected_df
                        st.session_state[selected_flag_key] = True
                        st.success(
                            f"✅ Successfully selected {len(selected_df)} items. Continuing..."
                        )
                        st.write("📤 Triggering rerun now.")
                        st.rerun()
            st.stop()

        # Step 4: Post-confirmation logic
        st.write("📦 Accessing confirmed selection...")
        confirmed_df = st.session_state[session_key]

        if confirmed_df is None or confirmed_df.empty:
            st.warning("⚠️ No confirmed rows found. Please re-select.")
            st.session_state[selected_flag_key] = False
            st.session_state[session_key] = None
            st.rerun()

        st.success(f"✅ Proceeding with {len(confirmed_df)} selected rows.")
        st.dataframe(confirmed_df, use_container_width=True, hide_index=True)

        return confirmed_df

    @staticmethod
    def get_job_openings(
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
        """
        This function is used to pull all the data from Rapid API
        """

        def log_progress(message):
            if status:
                status.write(message)
            else:
                print(message)

        inserter = InsertData()
        inserter.ensure_indexes(client)

        # ---------------------------- Job Data ---------------------------- #
        @retry(tries=5, delay=2, backoff=2)
        def fetch_all_jobs(keywords, **kwargs):
            if isinstance(keywords, str):
                keyword_list = [k.strip() for k in keywords.split(",") if k.strip()]
            elif isinstance(keywords, list):
                keyword_list = [str(k).strip() for k in keywords if str(k).strip()]
            else:
                raise ValueError("keywords must be a string or a list of strings")

            all_jobs = []
            for kw in keyword_list:
                try:
                    response = RapidAPI().search_jobs(keywords=kw, **kwargs)
                    jobs = response.get("data", [])
                    log_progress(f"Fetched {len(jobs)} jobs for keyword '{kw}'")
                    all_jobs.extend(jobs)
                except Exception as e:
                    log_progress(f"Error fetching jobs for keyword '{kw}': {e}")
            return all_jobs

        job_args = dict(
            location=location,
            date_posted=date_posted,
            job_type=job_type,
            function_id=function_id,
            industry_id=industry_id,
            onsite_remote=onsite_remote,
            sort=sort,
        )

        log_progress("🔍 Fetching jobs from Rapid API...")
        jobs_raw = fetch_all_jobs(keywords=keywords, **job_args)
        helper = HelperFunctions()
        jobs_df = pd.DataFrame([helper.flatten_dict(job) for job in jobs_raw])
        jobs_df.rename(columns={"id": "job_id"}, inplace=True)

        if jobs_df is not None and not jobs_df.empty:
            jobs_df = jobs_df.head(10)

        log_progress(f"📦 Total jobs fetched: {len(jobs_df)}")

        if jobs_df is None or len(jobs_df) == 0:
            if status:
                status.update(label="❌ No jobs found", state="error")
            st.warning(
                "⚠️ No jobs found for the given filters. Please try again with different filter combinations."
            )
            st.stop()

        # Check if we have pulled new companies or these are old comapnies

        # ✅ Step 1: Extract all company names from jobs_df
        company_names = jobs_df["company_name"].dropna().unique().tolist()

        # ✅ Example using get_database() method
        db = client.get_collection("FinalData")  # or client.db if it’s a property

        existing_docs = db.find({"company": {"$in": company_names}}, {"company": 1})
        existing_company_names = {doc["company"] for doc in existing_docs}

        # ✅ Step 3: Filter out rows with existing companies
        if existing_company_names:
            jobs_df = jobs_df[
                ~jobs_df["company_name"].isin(existing_company_names)
            ].reset_index(drop=True)
            log_progress(
                f"⚠️ Skipped {len(existing_company_names)} existing companies from FinalData: "
                f"{', '.join(existing_company_names)}"
            )

        # ✅ Step 4: If nothing left after filtering, stop the flow
        if jobs_df.empty:
            st.warning(
                "⚠️ All fetched jobs are from companies that already exist in the database. "
                "Try again with different filters."
            )
            if status:
                status.update(label="⚠️ No new companies to process", state="error")
            st.stop()

        # ------------------------------------------  Filter Option ------------------------------------------
        # jobs_df = JobOpenings().select_rows_from_dataframe(
        #     jobs_df, ["job_id", "company_name", "title", "url"]
        # )
        # ------------------------------------------  End of Filter Option ------------------------------------------
        inserter.insert_or_upsert_to_mongo(
            client, "RawJobs", inserter.prepare_data(jobs_df)
        )

        jobs_df.drop(
            columns=[
                col
                for col in [
                    "referenceId",
                    "posterId",
                    "company_logo",
                    "postedTimestamp",
                ]
                if col in jobs_df
            ],
            inplace=True,
        )
        jobs_df.rename(columns={"url": "job_url"}, inplace=True)

        def fetch_people_by_company(company: str, search_keywords: list):
            results = []
            for keyword in search_keywords:
                try:
                    response = RapidAPI().search_people(
                        keywords=keyword, company=company
                    )
                    items = response.get("data", {}).get("items", [])
                    for item in items:
                        item["Company"] = company
                    results.extend(items)

                    # ✅ Stop early if we've found 5 to 10 leads already
                    if 5 <= len(results) <= 10:
                        logger.info(
                            f"Enough leads found for {company}, skipping remaining keywords."
                        )
                        break

                except Exception as e:
                    logger.info(
                        f"Failed fetching people for {company}, with keyword {keyword}: {e}"
                    )
            return results

        def collect_people_data(df):
            companies = df["company_name"].dropna().unique()
            search_keywords = [
                "Human Resource, HR",
                "Talent Acquisition, IT Recruiter, VP",
                "CTO, Chief Technology Officer, COO, CXO",
                "Founder, Co-Founder, CEO, MD, Director",
                # HR, Talent Acquistion, IT Recruiter, VP >>>> CTO, COO, CXO, VP >>>> CEO, CO-Founder, MD, Director
            ]
            people_data = [
                person
                for company in companies
                for person in fetch_people_by_company(company, search_keywords)
            ]
            if not people_data:
                log_progress("No people data found.")
                return pd.DataFrame()
            log_progress(f"Retrieved {len(people_data)} company people records.")
            return pd.DataFrame(people_data)

        log_progress("👥 Fetching people data...")
        people_df = collect_people_data(jobs_df)

        if people_df["profileURL"].dropna().nunique() == 0:
            logger.info("No valid people with profile URLs found. Stopping the flow.")
            st.warning("⚠️ No hiring manager data found. Try different filters.")
            st.stop()

        # @retry(tries=2, delay=1)
        # def fetch_profile(link):
        #     try:
        #         profile = RapidAPI().get_linkedin_profile_data_by_url(link)
        #         if profile:
        #             profile["profileURL"] = link
        #         return profile
        #     except Exception as e:
        #         log_progress(f"Error fetching profile {link}: {e}")
        #         return {}

        @retry(tries=5, delay=2, backoff=2)  # Exponential backoff: 2s, 4s, 8s, ...
        def fetch_profile(link):
            try:
                response = RapidAPI().get_linkedin_profile_data_by_url(link)
                if isinstance(response, requests.Response):
                    if response.status_code == 429:
                        raise requests.exceptions.HTTPError("429 Too Many Requests")
                if response:
                    response["profileURL"] = link
                return response
            except requests.exceptions.HTTPError as e:
                if "429" in str(e):
                    log_progress(f"⚠️ Rate limit hit for {link}. Retrying...")
                    raise  # Retry decorator will handle backoff and retry
                else:
                    log_progress(f"❌ HTTPError for {link}: {e}")
            except Exception as e:
                log_progress(f"❌ General error fetching {link}: {e}")
            return {}

        log_progress("📄 Fetching LinkedIn profiles...")
        profiles = []
        for link in people_df["profileURL"].dropna().unique():
            profile_data = fetch_profile(link)
            profiles.append(profile_data)
            time.sleep(5)  # Add delay between each API call

        profiles_df = pd.DataFrame(profiles)
        profiles_df = pd.merge(
            profiles_df,
            people_df[["profileURL", "Company"]],
            on="profileURL",
            how="left",
        )
        inserter.insert_or_upsert_to_mongo(
            client, "RawPeople", inserter.prepare_data(profiles_df)
        )

        selected = [
            "id",
            "profileURL",
            "Company",
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
        final_people = profiles_df[
            [col for col in selected if col in profiles_df.columns]
        ].copy()
        final_people["processed_fullPositions"] = (
            final_people["fullPositions"].dropna().apply(helper.process_full_positions)
        )
        final_people["latest_experience"] = final_people.apply(
            lambda row: helper.find_relevant_experience(
                row["processed_fullPositions"], None
            ),
            axis=1,
        )
        final_people = pd.concat(
            [
                final_people.drop(
                    columns=["latest_experience", "geo"], errors="ignore"
                ),
                pd.json_normalize(final_people["latest_experience"]),
                pd.json_normalize(final_people["geo"]),
            ],
            axis=1,
        )
        final_people["clean_skills"] = final_people["skills"].apply(
            helper.process_skills
        )
        final_people.rename(
            columns={"Company": "company", "full": "full_address"}, inplace=True
        )
        final_people.drop(
            columns=[
                col
                for col in [
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
                if col in final_people
            ],
            inplace=True,
        )
        final_people = final_people[
            final_people["company"] == final_people["companyName"]
        ].reset_index(drop=True)
        final_people = final_people.drop_duplicates(subset=["profileURL"]).reset_index(
            drop=True
        )

        @retry(tries=5, delay=2, backoff=2)
        def fetch_posts(username):
            try:
                posts = (
                    RapidAPI().get_linkedin_posts_by_username(username).get("data", [])
                )
                for post in posts:
                    post["username"] = username
                return posts
            except Exception as e:
                log_progress(f"Error fetching posts for {username}: {e}")
                return []

        log_progress("📝 Fetching LinkedIn posts...")
        posts = [
            post
            for user in final_people["username"].dropna().unique()
            for post in fetch_posts(user)
        ]
        posts_df = pd.DataFrame(posts)

        # Proceed only if posts_df is not empty
        if not posts_df.empty:
            inserter.insert_or_upsert_to_mongo(
                client, "RawPosts", inserter.prepare_data(posts_df)
            )

            # Drop unnecessary columns if they exist
            drop_columns = [
                "isBrandPartnership",
                "totalReactionCount",
                "likeCount",
                "empathyCount",
                "commentsCount",
                "shareUrl",
                "postedAt",
                "postedDateTimestamp",
                "urn",
                "company",
                "document",
                "celebration",
                "entity",
                "companyMentions",
                "InterestCount",
                "praiseCount",
                "repostsCount",
                "image",
                "mentions",
                "appreciationCount",
                "video",
                "funnyCount",
                "article",
            ]
            posts_df.drop(columns=drop_columns, inplace=True, errors="ignore")

            # Clean and assign new columns
            posts_df = posts_df.assign(
                repost=posts_df.get("reposted", False).fillna(False),
                author=posts_df["author"].apply(helper.process_post_author),
                resharedPost=posts_df["resharedPost"].apply(
                    helper.process_reshared_data
                ),
            ).rename(columns={"Username": "username"})

        @retry(tries=5, delay=2, backoff=2)
        def fetch_company(cid):
            try:
                data = RapidAPI().get_linkedin_company_details_by_id(cid)
                return data.get("data", {})
            except Exception as e:
                log_progress(f"Error fetching company for ID {cid}: {e}")
                return {}

        log_progress("🏢 Fetching company info...")
        company_data = []
        for cid in final_people["companyId"].dropna().unique():
            try:
                company = fetch_company(int(cid))
                company_data.append(company)
            except Exception:
                continue

        company_df = pd.DataFrame(company_data).dropna(how="all").reset_index(drop=True)
        company_df.rename(columns={"id": "companyId"}, inplace=True)
        inserter.insert_or_upsert_to_mongo(
            client, "RawCompany", inserter.prepare_data(company_df)
        )
        company_df.drop(
            columns=[
                "Images",
                "isClaimable",
                "backgroundCoverImages",
                "logos",
                "callToAction",
                "followerCount",
                "featuredCustomers",
                "pageVerification",
            ],
            inplace=True,
            errors="ignore",
        )
        if "founded" in company_df:
            founded_df = pd.json_normalize(company_df["founded"])
            company_df.drop(columns=["founded"], inplace=True)
            company_df = company_df.join(
                founded_df.rename(columns={"year": "founded_year"})
            )

        inserter.insert_or_upsert_to_mongo(
            client, "Jobs", inserter.prepare_data(jobs_df)
        )
        inserter.insert_or_upsert_to_mongo(
            client, "People", inserter.prepare_data(final_people)
        )
        inserter.insert_or_upsert_to_mongo(
            client, "Posts", inserter.prepare_data(posts_df)
        )
        inserter.insert_or_upsert_to_mongo(
            client, "Company", inserter.prepare_data(company_df)
        )

        log_progress("✅ Data fetched and stored successfully.")
        return jobs_df, final_people, posts_df, company_df

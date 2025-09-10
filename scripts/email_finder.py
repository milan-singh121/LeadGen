"""
This scripts is used to pull emails data from Snov.io
"""

import sys
import os
import json
import logging
import time
from typing import Optional
import requests
import pandas as pd
import tldextract
from ast import literal_eval

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.configuration_vars import ConfigVars
from config.singleton import Singleton

logger = logging.getLogger(__name__)


class SnovEmailFinder(metaclass=Singleton):
    """
    This class contains function that help in finding email ids of prospets.
    """

    @staticmethod
    def get_access_token():
        """
        Generate Access Token for Snov.io API
        """
        url = "https://api.snov.io/v1/oauth/access_token"
        data = {
            "grant_type": "client_credentials",
            "client_id": literal_eval(ConfigVars().snov_user_id),
            "client_secret": literal_eval(ConfigVars().snov_secret_key),
        }
        response = requests.post(url, data=data)
        return response.json()["access_token"]

    def emails_by_domain_by_name_search(self, first_name, last_name, domain):
        """ "
        Finding email ids using first_name, last_name, and company domain
        """
        token = self.get_access_token()
        headers = {
            "authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        payload = json.dumps(
            {
                "rows": [
                    {"first_name": first_name, "last_name": last_name, "domain": domain}
                ],
                "webhook_url": "https://hooks.yourdomain.com",
            }
        )

        res = requests.post(
            "https://api.snov.io/v2/emails-by-domain-by-name/start",
            data=payload,
            headers=headers,
        )

        return json.loads(res.text)

    def emails_by_domain_by_name_result(self, task_hash):
        """
        Get email id result data
        """
        token = self.get_access_token()
        task_hash = task_hash
        headers = {"authorization": f"Bearer {token}"}

        params = {"task_hash": task_hash}

        res = requests.get(
            "https://api.snov.io/v2/emails-by-domain-by-name/result",
            params=params,
            headers=headers,
        )

        return json.loads(res.text)

    @staticmethod
    def flatten_snov_response(response):
        """Unpacks a Snov.io API response into a flat dict for DataFrame use"""

        # Default flat structure
        row = {}

        # Unpack meta data
        meta = response.get("meta", {})
        meta_rows = meta.get("rows", [{}])[0]
        row["first_name"] = meta_rows.get("first_name")
        row["last_name"] = meta_rows.get("last_name")
        row["domain"] = meta_rows.get("domain")
        row["task_hash"] = meta.get("task_hash")

        # Unpack data section
        data_entry = response.get("data", [{}])[0]
        row["full_name"] = data_entry.get("people")

        result = data_entry.get("result", [{}])[0]
        row["email"] = result.get("email")
        row["smtp_status"] = result.get("smtp_status")
        row["is_valid_format"] = result.get("is_valid_format")
        row["is_disposable"] = result.get("is_disposable")
        row["is_webmail"] = result.get("is_webmail")
        row["is_gibberish"] = result.get("is_gibberish")

        # Unpack top-level status
        row["status"] = response.get("status")

        # Convert to DataFrame
        return pd.DataFrame([row])

    def find_email_from_name_and_domain(
        self, first_name: str, last_name: str, domain: str, delay_seconds: int = 30
    ) -> Optional[pd.DataFrame]:
        """
        Finds a prospect's email address using first name, last name, and company
        domain via the Snov.io API.

        Parameters:
            first_name (str): The first name of the prospect.
            last_name (str): The last name of the prospect.
            domain (str): The company domain (e.g., 'example.com').
            delay_seconds (int): Optional delay before fetching result (Snov.io needs
                                    time to process the task).

        Returns:
            pd.DataFrame or None: A single-row DataFrame containing the email and associated
                    metadata if found, or None if an error occurred or no email was found.
        """
        try:
            # Start task
            task_data = self.emails_by_domain_by_name_search(
                first_name, last_name, domain
            )
            task_hash = task_data.get("data", []).get("task_hash", [])

            if not task_hash:
                raise ValueError(f"No task_hash returned: {task_data}")

            # Wait before polling results
            time.sleep(delay_seconds)

            # Fetch result
            email_data = self.emails_by_domain_by_name_result(task_hash)

            # Unpack
            unpacked = self.flatten_snov_response(email_data)

            return unpacked

        except Exception as e:
            # You can also log this if running in production
            print("Error finding email: %s", e)
            return None

    def add_url_for_search(self, url):
        token = self.get_access_token()
        params = {"access_token": token, "url": url}

        res = requests.post("https://api.snov.io/v1/add-url-for-search", data=params)

        return json.loads(res.text)

    def get_emails_from_url(self, url):
        token = self.get_access_token()
        params = {"access_token": token, "url": url}

        res = requests.post("https://api.snov.io/v1/get-emails-from-url", data=params)

        return json.loads(res.text)

    @staticmethod
    def flatten_person_data(data):
        flat = {}

        # These nested keys will be expanded separately
        nested_keys = ["currentJob", "previousJob", "social"]

        # Include all top-level keys except nested ones we handle separately
        for key, value in data.items():
            if key not in nested_keys:
                flat[key] = (
                    value if value is not None else None
                )  # Explicitly preserve None

        # Define expected sub-keys for currentJob and social
        current_job_keys = [
            "companyName",
            "position",
            "socialLink",
            "site",
            "locality",
            "state",
            "city",
            "street",
            "street2",
            "postal",
            "founded",
            "startDate",
            "endDate",
            "size",
            "industry",
            "companyType",
            "country",
        ]
        social_keys = ["link", "source"]

        # Flatten currentJob[0] if exists
        current_job = data.get("currentJob", [{}])
        job_data = current_job[0] if current_job else {}
        for key in current_job_keys:
            flat[f"currentJob_{key}"] = job_data.get(key, None)

        # Flatten social[0] if exists
        social = data.get("social", [{}])
        social_data = social[0] if social else {}
        for key in social_keys:
            flat[f"social_{key}"] = social_data.get(key, None)

        # Ensure 'emails' and 'previousJob' are explicitly preserved
        flat["emails"] = data.get("emails", None)
        flat["previousJob"] = data.get("previousJob", None)

        return flat

    @staticmethod
    def extract_emails(email_data):
        if not email_data:
            return None  # or return '' if you prefer empty string

        emails = [item["email"] for item in email_data if "email" in item]
        return ", ".join(emails) if emails else None

    @staticmethod
    def extract_domain(url):
        if not isinstance(url, str) or not url:
            return None
        extracted = tldextract.extract(url)
        if extracted.domain and extracted.suffix:
            return f"{extracted.domain}.{extracted.suffix}"
        return None

    def enrich_missing_emails(self, email_df: pd.DataFrame) -> pd.DataFrame:
        """
        Enrich missing emails in the given DataFrame using first name, last name, and domain.

        Parameters:
        - email_df (pd.DataFrame): DataFrame with columns ['firstName', 'lastName', 'domain', 'emails']
        - email_finder (object): An object with a method `.find_email_from_name_and_domain(first, last, domain)`
                                which returns a DataFrame with 'first_name', 'last_name', 'domain', 'email'

        Returns:
        - pd.DataFrame: The original DataFrame with 'emails' filled where possible using the finder
        """
        # Ensure required columns are present
        required_cols = {"firstName", "lastName", "domain", "emails"}
        if not required_cols.issubset(email_df.columns):
            raise ValueError(f"Input DataFrame must contain columns: {required_cols}")

        # Filter rows where emails are missing
        emails_missing = email_df[email_df["emails"].isna()]

        # Collect email search results
        results = []
        for _, row in emails_missing.iterrows():
            first = row["firstName"]
            last = row["lastName"]
            domain = row["domain"]
            try:
                result_df = self.find_email_from_name_and_domain(first, last, domain)
                results.append(result_df)
            except Exception:
                continue

        # Return original dataframe if all results are None or results is empty
        if not results or all(r is None for r in results):
            return email_df

        # Remove None entries before concatenation
        valid_results = [r for r in results if r is not None]

        if not valid_results:
            return email_df

        # Concatenate all found emails
        enriched_df = pd.concat(valid_results, ignore_index=True)
        enriched_df = enriched_df[enriched_df["email"].notna()]
        enriched_df = enriched_df.rename(
            columns={"first_name": "firstName", "last_name": "lastName"}
        )

        # Merge enriched emails back into original DataFrame
        merged_df = pd.merge(
            email_df,
            enriched_df[["firstName", "lastName", "domain", "email"]],
            on=["firstName", "lastName", "domain"],
            how="left",
        )

        # Fill 'emails' only where missing
        merged_df.loc[
            merged_df["emails"].isna() & merged_df["email"].notna(), "emails"
        ] = merged_df["email"]

        # Drop the temporary 'email' column
        merged_df = merged_df.drop(columns=["email"])

        return merged_df

    def collect_emails_from_linkedin_urls(
        self, people_df: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Fetch and process email data from LinkedIn profile URLs.

        Parameters:
        - people_df (pd.DataFrame): DataFrame with a 'profileURL' column.

        Returns:
        - pd.DataFrame: Processed email data with profile URL, extracted emails, and domains.
        """

        email_records = []

        for linkedin_url in people_df["profileURL"].dropna().unique():
            try:
                response = self.add_url_for_search(linkedin_url)
                url_result = self.get_emails_from_url(linkedin_url)
                flattened = self.flatten_person_data(url_result.get("data", None))
                flattened["profileURL"] = linkedin_url
                email_records.append(flattened)
                # logger.info(f"Email data fetched for {linkedin_url}, {flattened}")
            except Exception as e:
                if logger:
                    logger.error(f"Error processing URL {linkedin_url}: {e}")
                continue

        if not email_records:
            return pd.DataFrame()

        email_df = pd.DataFrame(email_records)

        if "emails" in email_df.columns:
            email_df["emails"] = email_df["emails"].apply(self.extract_emails)
        else:
            email_df["emails"] = None

        if "currentJob_site" in email_df.columns:
            email_df["domain"] = email_df["currentJob_site"].apply(self.extract_domain)
        else:
            email_df["domain"] = None

        return email_df

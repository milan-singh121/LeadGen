"""
This scripts is used to pull data from Rapid API for Lead Gen.
"""

import sys
import os
import time
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import requests
from typing import Dict, Any, Optional
import logging
from ast import literal_eval
from config.singleton import Singleton
from config.configuration_vars import ConfigVars

logger = logging.getLogger(__name__)


class RapidAPI(metaclass=Singleton):
    """
    A singleton class to interact with the LinkedIn Data API via RapidAPI.

    This class provides methods to search for jobs, people, and retrieve profile,
    company, and post data using various endpoints from the RapidAPI platform.
    """

    def __init__(self) -> None:
        """Initialize with base URL and API key from configuration."""
        config = ConfigVars()
        raw_url = literal_eval(config.rapid_api_base_url.strip().rstrip("/"))

        # Ensure scheme is present
        if not raw_url.startswith("http://") and not raw_url.startswith("https://"):
            raw_url = f"https://{raw_url}"

        self.base_url: str = raw_url
        self.api_key: str = literal_eval(config.rapid_api_key)
        self.headers: Dict[str, str] = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self._extract_host(self.base_url),
            "Content-Type": "application/json",
        }

    def _extract_host(self, url: str) -> str:
        """
        Extract the host portion from a full URL.

        Args:
            url (str): Full URL.

        Returns:
            str: Host name.
        """
        return url.replace("https://", "").replace("http://", "").split("/")[0]

    def _make_request(
        self, endpoint: str, params: Dict[str, Any], delay_seconds: float = 5.0
    ) -> Optional[Dict[str, Any]]:
        """
        Internal method to perform a GET request to a specific API endpoint.

        Args:
            endpoint (str): API endpoint to call.
            params (Dict[str, Any]): Dictionary of query parameters.
            delay_seconds (float): Delay before each request to avoid throttling.

        Returns:
            Optional[Dict[str, Any]]: Parsed JSON response or None if the request fails.
        """
        url = f"{self.base_url}{endpoint}"
        try:
            logger.info(f"GET {url} | Params: {params}")
            time.sleep(delay_seconds + random.uniform(0.5, 1.5))  # jitter
            response = requests.get(
                url, headers=self.headers, params=params, timeout=30
            )
            response.raise_for_status()
            try:
                return response.json()
            except ValueError as e:
                logger.error(f"Invalid JSON response from {url}: {e}")
                return None
        except requests.HTTPError as e:
            logger.error(
                f"HTTPError for {url}: {e} | Response: {e.response.text if e.response else 'No response'}"
            )
        except requests.RequestException as e:
            logger.error(f"Request to {url} failed: {e}")
        return None

    def search_jobs(
        self,
        keywords: Optional[str] = None,
        location: Optional[str] = None,
        job_type: Optional[str] = None,
        function_id: Optional[str] = None,
        industry_id: Optional[str] = None,
        onsite_remote: Optional[str] = None,
        # title_id: str,
        # experience_level: Optional[str],
        sort: str = "mostRecent",
        date_posted: str = "pastMonth",
    ) -> Optional[Dict[str, Any]]:
        """
        Search job postings with various filters.

        Args:
            keywords (str): Keywords to search for (e.g., "software engineer").
            location (str): LinkedIn location ID (e.g., "103644278" for United States).
            job_type (str): Type of job (e.g., "F" for Full-time, "C" for Contract).
            title_id (str): LinkedIn title ID.
            function_id (str): LinkedIn function ID.
            industry_id (str): LinkedIn industry ID.
            onsite_remote (str): Onsite/remote preference (e.g., "hybrid", "remote", "onSite").
            experience_level (Optional[str]): Experience level
                (e.g., "1" for Entry level, "6" for Executive).
            sort (str, optional): Sort order for results. Defaults to "mostRecent".
                                  Other options include "mostRelevant".
            date_posted (str, optional): Time frame for when the job was posted.
                    Defaults to "pastMonth". Other options include "past24Hours", "pastWeek".

        Returns:
            Optional[Dict[str, Any]]: Job search results.
        """
        payload = self._make_request(
            "/search-jobs",
            {
                "keywords": keywords,
                "locationId": location,
                "datePosted": date_posted,
                "jobType": job_type,
                "functionIds": function_id,
                "industryIds": industry_id,
                "onsiteRemote": onsite_remote,
                "sort": sort,
                "start": "0",
            },
        )

        return {k: v for k, v in payload.items() if v is not None}

    def get_hiring_team(self, job_id: str, job_url: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve hiring team information for a specific job.

        Args:
            job_id (str): The LinkedIn job ID.
            job_url (str): The URL of the LinkedIn job posting.


        Returns:
            Optional[Dict[str, Any]]: Hiring team data.
        """
        return self._make_request("/get-hiring-team", {"id": job_id, "url": job_url})

    def search_people(
        self,
        keywords: str,
        company: str,  # keyword_title: str, geo: str,
    ) -> Optional[Dict[str, Any]]:
        """
        Search LinkedIn people by filters such as geo and title.

        Args:
            keywords (str): Keywords to search for (e.g., "John Doe").
            geo (str): LinkedIn geo ID for location filtering.
            keyword_title (str): Keywords to search within job titles (e.g., "Software Engineer").
            company (str): LinkedIn company ID or name to filter by current company.


        Returns:
            Optional[Dict[str, Any]]: People search results.
        """
        return self._make_request(
            "/search-people",
            {
                "keywords": keywords,
                "start": "0",
                "company": company,
            },
        )

    def get_linkedin_profile_data_by_url(
        self, profile_url: str
    ) -> Optional[Dict[str, Any]]:
        """
        Fetch LinkedIn profile data using a public profile URL.

        Args:
            profile_url (str): LinkedIn profile URL.

        Returns:
            Optional[Dict[str, Any]]: Profile data.
        """
        return self._make_request("/get-profile-data-by-url", {"url": profile_url})

    def get_linkedin_posts_by_username(self, username: str) -> Optional[Dict[str, Any]]:
        """
        Get the last 50 LinkedIn posts from a user by username.

        Args:
            username (str): LinkedIn username.

        Returns:
            Optional[Dict[str, Any]]: Post data.
        """
        return self._make_request("/get-profile-posts", {"username": username})

    def get_linkedin_profile_comments(self, username: str) -> Optional[Dict[str, Any]]:
        """
        Get the last 50 comments made by a LinkedIn user.

        Args:
            username (str): LinkedIn username.

        Returns:
            Optional[Dict[str, Any]]: Comment data.
        """
        return self._make_request("/get-profile-comments", {"username": username})

    def get_linkedin_company_details_by_id(self, company_id: int) -> bytes:
        """
        Fetch company details using a LinkedIn Company ID

        Args:
            username (str): LinkedIn company ID

        Returns:
            Optional[Dict[str, Any]]: Company details.
        """
        return self._make_request("/get-company-details-by-id", {"id": company_id})

    def get_linkedin_company_details_by_username(self, username: str):
        """
        Fetch company details using a LinkedIn Company Username

        Args:
            username (str): LinkedIn company ID

        Returns:
            Optional[Dict[str, Any]]: Company details.
        """

        return self._make_request("/get-company-details", {"username": username})

    def get_company_posts_by_username(self, username: str):
        """
        Fetch company linkedin posts using a LinkedIn Company Username

        Args:
            username (str): LinkedIn company username

        Returns:
            Optional[Dict[str, Any]]: Company details.
        """

        return self._make_request("/get-company-posts", {"username": username})

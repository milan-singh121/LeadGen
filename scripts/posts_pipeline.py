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
from datetime import datetime, timedelta


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


class PostsFetcherPipeline:
    def __init__(self, mongo_client, status=None):
        self.client = mongo_client
        self.raw_collection = mongo_client.get_collection("RawPosts")
        self.clean_collection = mongo_client.get_collection("Posts")
        self.helper = HelperFunctions()
        self.inserter = InsertData()
        self.status = status or st.status(
            "📝 Fetching LinkedIn posts...", expanded=True
        )

    def fetch_existing_posts(self, username):
        """Return posts from last 30 days for given username."""
        cutoff_date = (datetime.utcnow() - timedelta(days=30)).isoformat()
        return list(
            self.raw_collection.find(
                {"username": username, "message_date": {"$gte": cutoff_date}},
                {"_id": 0, "message_date": 0},
            )
        )

    @retry(tries=5, delay=2, backoff=2)
    def fetch_posts_for_user(self, username):
        try:
            posts = RapidAPI().get_linkedin_posts_by_username(username).get("data", [])
            for post in posts:
                post["username"] = username
            return posts
        except Exception as e:
            logger.warning(f"Error fetching posts for {username}: {e}")
            return []

    def get_new_posts(self, usernames):
        """Return existing posts if present, else fetch from API and return."""
        all_posts = []

        for username in usernames:
            existing = self.fetch_existing_posts(username)

            if existing:
                logger.info(f"✅ Found {len(existing)} posts in DB for {username}")
                all_posts.extend(existing)
            else:
                logger.info(f"🔍 No posts in DB for {username}, calling API...")
                posts = self.fetch_posts_for_user(username)
                all_posts.extend(posts)
                time.sleep(1)

        return pd.DataFrame(all_posts)

    def clean_posts(self, posts_df):
        """Drop irrelevant fields and standardize structure."""
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

        posts_df = posts_df.assign(
            repost=posts_df.get("reposted", False).fillna(False),
            author=posts_df["author"].apply(self.helper.process_post_author),
            resharedPost=posts_df["resharedPost"].apply(
                self.helper.process_reshared_data
            ),
        ).rename(columns={"Username": "username"})

        return posts_df

    def run(self, final_people_df):
        self.status.write("📝 Fetching LinkedIn posts...")
        usernames = final_people_df["username"].dropna().unique()
        posts_df = self.get_new_posts(usernames)

        if posts_df.empty:
            self.status.write("📝 No posts found.")
            return pd.DataFrame()

        self.inserter.insert_or_upsert_to_mongo(
            self.client, "RawPosts", self.inserter.prepare_data(posts_df)
        )

        clean_df = self.clean_posts(posts_df)
        self.inserter.insert_or_upsert_to_mongo(
            self.client, "Posts", self.inserter.prepare_data(clean_df)
        )

        self.status.write(f"✅ {len(clean_df)} posts processed.")
        return clean_df

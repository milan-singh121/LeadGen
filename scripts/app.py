import sys
import os
import threading
import json
import logging
from pymongo import MongoClient
import warnings
from ast import literal_eval
import uuid
import pandas as pd

warnings.filterwarnings("ignore")

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
app_dir = os.path.dirname(os.path.abspath(__file__))

# Project root is one level up from scripts/
project_root = os.path.abspath(os.path.join(app_dir, ".."))

# Insert project root into sys.path (if not already there)
if project_root not in sys.path:
    sys.path.insert(0, project_root)


from config.singleton import Singleton
from config.configuration_vars import ConfigVars
from scripts.main import LeadGen
from scripts.insert_data_in_db import InsertData
from scripts.mongo_client import MongoDBClient

import streamlit as st

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger(__name__)

# Apply Streamlit styling
st.set_page_config(page_title="LeadGen Search", layout="wide")
st.markdown(
    """
    <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            font-size: 16px;
        }
        .title {
            font-size: 2.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: var(--text-color);
        }
        .subheader {
            font-size: 1.2rem;
            font-weight: 500;
            margin-top: 2rem;
            margin-bottom: 0.5rem;
            color: var(--text-color);
        }
        :root {
            --text-color: #FFFFFF;
        }
        @media (prefers-color-scheme: light) {
            :root {
                --text-color: #31333F;
            }
        }
    </style>
""",
    unsafe_allow_html=True,
)


industries_col = MongoDBClient().get_collection("IndustryCodesV2")
functions_col = MongoDBClient().get_collection("JobFunctionID")
locations_col = MongoDBClient().get_collection("LocationID")


# Fetch dropdown data from MongoDB
def get_dropdown_data(collection):
    data = list(collection.find({}, {"_id": 0, "ID": 1, "Description": 1}))
    desc_to_id = {item["Description"]: item["ID"] for item in data}
    options = ["-- None --"] + list(desc_to_id.keys())
    return options, desc_to_id


# UI inputs
st.markdown(
    "<div class='title'>Lead Generation Job Search</div>", unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    keywords = st.text_input("🔍 Job Title Keywords (comma-separated)")
    job_type = st.selectbox(
        "🧰 Job Type", ["-- None --", "fullTime", "partTime", "contract", "internship"]
    )
    job_type_value = None if job_type == "-- None --" else job_type

with col2:
    date_posted = st.selectbox(
        "📅 Date Posted", ["pastMonth", "anyTime", "pastWeek", "past24Hours"]
    )


with col3:
    onsite_remote = st.selectbox(
        "🏢 Onsite/Remote", ["-- None --", "onSite", "remote", "hybrid"]
    )
    onsite_remote_value = None if onsite_remote == "-- None --" else onsite_remote
#     sort = st.selectbox("🔽 Sort By", ["mostRelevant", "mostRecent"])
sort = "mostRecent"

st.markdown(
    "<div class='subheader'>📍 Location, Industry, and Function</div>",
    unsafe_allow_html=True,
)
col4, col5, col6 = st.columns([1, 1, 1])

location_options, location_map = get_dropdown_data(locations_col)
industry_options, industry_map = get_dropdown_data(industries_col)
function_options, function_map = get_dropdown_data(functions_col)

with col4:
    selected_location = st.selectbox("🌐 Location", location_options, index=0)

with col5:
    selected_industry = st.selectbox("🏭 Industry", industry_options, index=0)

with col6:
    selected_function = st.selectbox("💼 Job Function", function_options, index=0)

# Run job search
st.markdown("<br>", unsafe_allow_html=True)
search_clicked = st.button("🚀 Search Jobs", use_container_width=True)

if search_clicked:
    location_id = (
        location_map.get(selected_location)
        if selected_location != "-- None --"
        else None
    )
    industry_id = (
        industry_map.get(selected_industry)
        if selected_industry != "-- None --"
        else None
    )
    function_id = (
        function_map.get(selected_function)
        if selected_function != "-- None --"
        else None
    )

    keyword_list = (
        [k.strip() for k in keywords.split(",") if k.strip()] if keywords else None
    )

    filters_log = {
        "keywords": keyword_list,
        "job_type": job_type_value,
        "date_posted": date_posted,
        "onsite_remote": onsite_remote_value,
        "sort": sort,
        "location": {"description": selected_location, "id": location_id},
        "industry": {"description": selected_industry, "id": industry_id},
        "job_function": {"description": selected_function, "id": function_id},
        "status": "Inprogress",
        "query_id": str(uuid.uuid4()),
    }

    # Store Query in DB
    client = MongoDBClient()
    inserter = InsertData()
    inserter.ensure_indexes(client)
    filter_log = pd.DataFrame([filters_log])
    prepared_query_data = inserter.prepare_data(filter_log)
    inserter.insert_or_upsert_to_mongo(client, "Query", prepared_query_data)

    logger.info(f"Selected Filters: {json.dumps(filters_log, indent=2)}")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.success("✅ Filters applied. Ready to fetch job data!")
    # st.json(filters_log)

    data = LeadGen().run_email_sequence_pipeline(
        keywords=keyword_list,
        location=location_id,
        date_posted=date_posted,
        job_type=job_type_value,
        function_id=function_id,
        industry_id=industry_id,
        onsite_remote=onsite_remote_value,
        sort=sort,
        query_data=prepared_query_data,
    )

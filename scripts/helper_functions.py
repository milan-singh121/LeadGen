"""
This script contains functions to process and clean LinkedIn Data
"""

import os
import sys
import ast
import json
import re
import pandas as pd
import logging
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.singleton import Singleton
from scripts.questionnaire_prompts import PromptsLib
from scripts.llm import ClaudeAIResponse

logger = logging.getLogger(__name__)


class HelperFunctions(metaclass=Singleton):
    """
    A collection of static helper functions for processing and cleaning LinkedIn data,
    often retrieved in string or complex dictionary/list formats.
    """

    @staticmethod
    def flatten_dict(d, parent_key="", sep="_"):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(HelperFunctions.flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    @staticmethod
    def find_relevant_experience(experiences, target_company=None):
        if isinstance(experiences, str):
            try:
                experiences = ast.literal_eval(experiences)
            except Exception:
                logging.warning(
                    f"Could not parse stringified experiences: {experiences}"
                )
                return None

        if not isinstance(experiences, list):
            logging.warning(f"Unexpected format for experiences: {experiences}")
            return None

        # 1. Prefer match on companyName
        if target_company:
            for val in experiences:
                if (
                    isinstance(val, dict)
                    and val.get("companyName", "").strip().lower()
                    == target_company.strip().lower()
                ):
                    return val

        # 2. Return first current role (no end date)
        for val in experiences:
            if not isinstance(val, dict):
                continue
            end_date = val.get("end", {})
            if all(end_date.get(k, 0) in [0, None] for k in ("year", "month", "day")):
                return val

        # 3. Fallback to first experience
        return experiences[0] if experiences else None

    @staticmethod
    def process_full_positions(entry):
        if isinstance(entry, str):
            try:
                entry = ast.literal_eval(entry)
            except (ValueError, SyntaxError):
                return []  # or log error, depending on use case
        elif not isinstance(entry, list):
            return []

        return [
            {
                "companyId": p.get("companyId", ""),
                "companyName": p.get("companyName", ""),
                "companyUsername": p.get("companyUsername", ""),
                "companyURL": p.get("companyURL", ""),
                "companyLogo": p.get("companyLogo", ""),
                "companyIndustry": p.get("companyIndustry", ""),
                "companyStaffCountRange": p.get("companyStaffCountRange", ""),
                "title": p.get("title", ""),
                "location": p.get("location", ""),
                "description": p.get("description", ""),
                "employmentType": p.get("employmentType", ""),
                "start": p.get("start", {}),
                "end": p.get("end", {}),
            }
            for p in entry
        ]

    @staticmethod
    def process_skills(entry):
        # Return empty list for NaN or None
        if entry is None or isinstance(entry, float) and pd.isna(entry):
            return []

        # If it's a string (e.g., from JSON or stringified list), try to parse
        if isinstance(entry, str):
            try:
                entry = ast.literal_eval(entry)
            except (ValueError, SyntaxError) as e:
                print(f"Error parsing string entry: {entry} -> {e}")
                return []

        # If it's already a list of dicts, extract 'name'
        if isinstance(entry, list):
            return [item.get("name", "") for item in entry if isinstance(item, dict)]

        # Fallback
        return []

    @staticmethod
    def process_post_author(entry):
        # If the entry is NaN or None
        if entry is None or isinstance(entry, float) and pd.isna(entry):
            return []

        # If it's a string, attempt to parse it
        if isinstance(entry, str):
            try:
                entry = ast.literal_eval(entry)
            except (ValueError, SyntaxError) as e:
                print(f"Error parsing author entry: {entry} -> {e}")
                return []

        # If it's a single dict (not a list), convert to a list
        if isinstance(entry, dict):
            entry = [entry]

        # If it's not a list at this point, return empty
        if not isinstance(entry, list):
            return []

        # Process the list of authors
        processed_author = [
            {
                "firstName": p.get("firstName", ""),
                "lastName": p.get("lastName", ""),
                "headline": p.get("headline", ""),
                "username": p.get("username", ""),
                "url": p.get("url", ""),
            }
            for p in entry
            if isinstance(p, dict)
        ]
        return processed_author

    @staticmethod
    def process_reshared_data(entry):
        # If the entry is NaN or None
        if entry is None or isinstance(entry, float) and pd.isna(entry):
            return []

        # If it's a string, attempt to parse it
        if isinstance(entry, str):
            try:
                entry = ast.literal_eval(entry)
            except (ValueError, SyntaxError) as e:
                print(f"Error parsing author entry: {entry} -> {e}")
                return []

        # If it's a single dict (not a list), convert to a list
        if isinstance(entry, dict):
            entry = [entry]

        # If it's not a list at this point, return empty
        if not isinstance(entry, list):
            return []

        # Process the list of authors
        processed_reshared = [
            {
                "text": p.get("text", ""),
                "postUrl": p.get("postUrl", ""),
                "author": p.get("author", ""),
                "author_url": p.get("url", ""),
                "url": p.get("url", ""),
            }
            for p in entry
            if isinstance(p, dict)
        ]
        return processed_reshared

    @staticmethod
    def parse_claude_response(claude_output: str):
        cleaned = claude_output.strip().replace("\\n", "").replace('\\"', '"')

        start = cleaned.find("[")
        end = cleaned.rfind("]") + 1
        json_like = cleaned[start:end]

        try:
            parsed = json.loads(json_like)
            return parsed
        except json.JSONDecodeError as e:
            print("Failed to parse response:", e)
            return []

    @staticmethod
    def clean_data_for_questionnaire(final_people_data, people_posts):
        # Clean People's Data
        people_dict = {
            f"Prospect {i + 1}": row
            for i, (_, row) in enumerate(
                final_people_data.drop(columns="processed_fullPositions").iterrows()
            )
        }

        # Merge name info into posts
        name_cols = ["username", "firstName", "lastName"]
        people_posts = pd.merge(
            people_posts, final_people_data[name_cols], on="username", how="left"
        )

        # Clean and filter post dates
        people_posts["postedDate"] = pd.to_datetime(
            people_posts["postedDate"].str.replace(" +0000 UTC", "", regex=False),
            errors="coerce",
        )
        cutoff_date = datetime.utcnow() - pd.DateOffset(months=2)

        # Filter recent, original posts
        recent_posts = people_posts[
            (people_posts["postedDate"] >= cutoff_date) & (~people_posts["repost"])
        ]

        return people_dict, recent_posts

    def get_questionnaire_data(self, jobs_df, company_df, final_people, posts_df):
        """
        This function is used to generate questionnaire results
        """
        questionnaire_data = []
        for company_name in list(jobs_df.company_name.dropna().unique()):
            sub_jobs_df = jobs_df[jobs_df["company_name"] == company_name]
            sub_company_df = company_df[company_df["name"] == company_name]
            sub_people_df = final_people[final_people["company"] == company_name]
            usernames = list(sub_people_df["username"].dropna().unique())
            sub_posts_df = posts_df[posts_df["username"].isin(usernames)]

            if sub_company_df.empty or sub_people_df.empty:
                continue

            sub_people_dict, sub_recent_posts = self.clean_data_for_questionnaire(
                sub_people_df, sub_posts_df
            )

            system_prompt, user_prompt = PromptsLib().question_summarizer_prompt(
                sub_jobs_df.to_dict(orient="records"),
                sub_company_df.to_dict(orient="records"),
                sub_people_dict,
                sub_recent_posts,
                PromptsLib().icp_definition_prompt(),
            )
            result = ClaudeAIResponse().get_claude_sonnet35_response(
                system_prompt, user_prompt
            )
            qa_list = HelperFunctions().parse_claude_response(result)

            # This step ensures a flat dict (question -> answer)
            qa_dict = {item["question"]: item["answer"] for item in qa_list}
            qa_dict["Company Name"] = company_name
            qa_dict_data = pd.DataFrame([qa_dict])

            questionnaire_data.append(qa_dict_data)

        questionnaire_response = pd.concat(questionnaire_data, ignore_index=True)

        logging.info("Questionnaire Results: %s", list(questionnaire_response.columns))
        return questionnaire_response

    @staticmethod
    def fix_bullet_breaks(email_body: str) -> str:
        # Ensure bullets are followed by a space if not already
        email_body = re.sub(r"•(?!\s)", "• ", email_body)

        # Ensure numbered bullets like "1.Something" have a space: "1. Something"
        email_body = re.sub(r"(\d+\.)(\S)", r"\1 \2", email_body)

        # Split on bullets for HTML formatting
        parts = re.split(r"(• )", email_body)
        rebuilt = ""
        for i in range(1, len(parts), 2):
            bullet = parts[i]
            content = parts[i + 1] if i + 1 < len(parts) else ""
            rebuilt += bullet + content.strip() + "<br>"

        return parts[0] + rebuilt if parts else email_body

    @staticmethod
    def fix_numbered_bullet_breaks(email_body: str) -> str:
        # Split using a lookahead for numbered bullets like 1., 2., 3.
        parts = re.split(r"(?=(?:\d{1,2}\.))", email_body)
        rebuilt = parts[0]  # start with the initial text before the first bullet

        for part in parts[1:]:
            # Only add <br> if it doesn't already end with a break
            if not part.strip().endswith("<br>"):
                rebuilt += part.strip() + "<br>"
            else:
                rebuilt += part

        return rebuilt

    @staticmethod
    def extract_questions_and_answers(row, question_fields):
        """
        Convert question-answer pairs into a nested 'questions' dict format.
        Only include fields that actually exist in the row (i.e., in the dataframe).
        """
        questions_dict = {}
        q_counter = 1

        for col in question_fields:
            if col in row and pd.notnull(row[col]):
                questions_dict[f"question_{q_counter}"] = col
                questions_dict[f"answer_{q_counter}"] = row[col]
                q_counter += 1

        return questions_dict

    @staticmethod
    def extract_emails(row, email_fields):
        """
        Bundle all Subject/Email Body pairs into a nested dict under 'emails'.
        """
        return {col: row[col] for col in email_fields}

    def format_final_data(self, final_data):
        """
        This function is used to format the final data into a proper structure
        """
        # Auto-detect all question columns (those that contain "?")
        question_columns = [
            "What is the full legal name of the company?",
            "What industry or niche do they primarily operate in?",
            "Where is the company headquartered (city & country)?",
            "What is the current estimated employee count?",
            "What is the company website URL as mentioned in the LinkedIn Data?",
            "Name of the individual",
            "Their job title or designation",
            "Are they likely a decision-maker (e.g., manager, VP, director, CXO)?",
            "Are they hiring for roles that suggest growth, scaling, or specific operational challenges? If yes, mention the roles.",
            "Based on the company's industry, employee size, and growth stage, does it align with the Ideal Customer Profile (ICP) outlined in the ICP definition? Provide a brief rationale for your assessment.",
            "Are they likely to have the budget and maturity to engage with our service/product?",
            "Have they posted or reshared any content that shows their pain points or areas of focus? Summarize relevant content if available.",
            "Mention any known external tools or platforms the company uses (e.g., CRMs, marketing automation, cloud platforms, AI tools).",
            "Can you derive a clear value proposition we might be able to offer, based on their context?",
        ]

        # Filter question_columns to include only those present in the dataframe
        valid_question_columns = [
            q for q in question_columns if q in final_data.columns
        ]

        # Transform and nest questions if any valid ones exist
        if valid_question_columns:
            final_data["questions"] = final_data.apply(
                lambda row: self.extract_questions_and_answers(
                    row, valid_question_columns
                ),
                axis=1,
            )
            final_data.drop(columns=valid_question_columns, inplace=True)
        else:
            final_data["questions"] = [{}] * len(final_data)

        # Define the subject and email body columns
        email_columns = [
            "Subject 1",
            "Subject 2",
            "Subject 3",
            "Subject 4",
            "Subject 5",
            "Email Body 1",
            "Email Body 2",
            "Email Body 3",
            "Email Body 4",
            "Email Body 5",
        ]

        # Apply transformation row-wise
        final_data["email_data"] = final_data.apply(
            lambda row: self.extract_emails(row, email_columns), axis=1
        )

        # Optional: drop the original flat columns
        final_data.drop(columns=email_columns, inplace=True)
        return final_data

    @staticmethod
    def clean_email(value):
        if isinstance(value, list) and value:
            return value[0]  # return first email from list
        elif isinstance(value, str):
            return value.strip()  # return as-is (after stripping whitespace)
        else:
            return None  # handle None or unexpected types

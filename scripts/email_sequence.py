"""
This script is used to generate email sequence.
"""

import os
import sys
import re
from typing import List, Dict
import pandas as pd


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.singleton import Singleton
from scripts.emails_prompt import EmailSequence
from scripts.helper_functions import HelperFunctions
from scripts.llm import ClaudeAIResponse


class GetEmailSequence(metaclass=Singleton):
    """
    This class is used to generate email sequence.
    """

    @staticmethod
    def extract_between_tags(tag: str, string: str, strip: bool = False) -> List[str]:
        """
        This function is used to extract between tags.
        """
        # Use regex to find all occurrences of the tag content
        ext_list = re.findall(f"<{tag}>(.+?)</{tag}>", string, re.DOTALL)
        if strip:
            ext_list = [e.strip() for e in ext_list]
        return ext_list

    def extract_email_details(self, email_content: str) -> Dict[str, str]:
        """
        This function is used to extract email details from the LLM response.
        """
        # Extract the content of each nested tag within an email
        variation = self.extract_between_tags("sequence", email_content, strip=True)
        subject = self.extract_between_tags("subject", email_content, strip=True)
        body = self.extract_between_tags("body", email_content, strip=True)
        # logic = extract_between_tags("logic", email_content, strip=True)

        return {
            "sequence": variation[0] if variation else "",
            "subject": subject[0] if subject else "",
            "body": body[0] if body else "",
            # "logic": logic[0] if logic else ""
        }

    def extract_emails(self, msg: str) -> List[Dict[str, str]]:
        """
        This function is used to extract emails from the LLM response.
        """
        # Extract the content within <emails> tag
        emails_content = self.extract_between_tags("emails", msg, strip=True)

        if not emails_content:
            return []

        # Extract each <email> tag within the <emails> content
        email_contents = self.extract_between_tags(
            "email", emails_content[0], strip=True
        )

        # Extract the details of each email
        emails = [
            self.extract_email_details(email_content)
            for email_content in email_contents
        ]

        return emails

    @staticmethod
    def clean_email_output(raw_email: str) -> str:
        """
        Cleans LLM-generated email content by:
        - Replacing <br><br> with <br>
        - Removing closing salutations (e.g., 'Best,<br>Ahmed')

        Args:
            raw_email (str): The original email text

        Returns:
            str: Cleaned email text
        """
        # Step 1: Normalize <br><br> to <br>
        # cleaned_email = raw_email.replace("<br><br>", "<br>")
        # cleaned_email = cleaned_email.replace("</b><br>", "</b>")

        # Step 2: Remove closing salutations (common formats like 'Best,<br>Name', 'Thanks,<br>Person')
        closing_salutation_pattern = r"(Best|Regards|Thanks|Thank you|Cheers|Warm regards|Best regards|Ahmed|Cheers, Ahmed|Best regards,|Best,)[\s,]*<br>.*?$"
        cleaned_email = re.sub(
            closing_salutation_pattern,
            "",
            raw_email,
            flags=re.IGNORECASE | re.DOTALL,
        )

        return cleaned_email.strip()

    @staticmethod
    def remove_line_breaks(text: str) -> str:
        if not isinstance(text, str):
            return text
        # Remove actual newline characters
        text = text.replace("\n", "")
        # Remove escaped newline strings (\\n)
        text = text.replace("\\n", "")
        return text.strip()

    def format_emails(self, all_emails):
        """
        This function is used to clean the email body to remove extra HTML breakers
        """
        email_body_cols = [
            col for col in all_emails.columns if col.startswith("Email Body")
        ]

        for col in email_body_cols:
            all_emails[col] = all_emails[col].apply(self.clean_email_output)
        return all_emails

    def generate_email_sequence(self, final_people, jobs_df, posts_df):
        """
        Generates a personalized email sequence for each prospect in final_people.
        """

        emails_dataframe = []

        email_seq_obj = EmailSequence()
        helper = HelperFunctions()
        claude = ClaudeAIResponse()

        for _, row in final_people.iterrows():
            try:
                first_name = row["firstName"]
                last_name = row["lastName"]
                profile_url = row["profileURL"]
                username = row["username"]
                headline = row.get("headline", "")
                summary = row.get("summary", "")
                full_positions = row.get("processed_fullPositions", "")
                skills = row.get("clean_skills", "")
                title = row.get("title", "")
                company_industry = row.get("companyIndustry", "")
                company = row.get("company", "")
                job_data = jobs_df[jobs_df["company_name"] == company]
                description = row.get("description", "")

                if not posts_df.empty:
                    posts = posts_df[posts_df["username"] == username]
                    _, recent_posts = helper.clean_data_for_questionnaire(
                        final_people, posts
                    )
                else:
                    recent_posts = []

                print(f"Generating for {first_name} {last_name}")

                email_user_prompt = email_seq_obj.get_email_user_prompt(
                    first_name,
                    last_name,
                    headline,
                    summary,
                    skills,
                    company_industry,
                    title,
                    description,
                    full_positions,
                    recent_posts,
                    job_data,
                )

                email_system_prompt = email_seq_obj.get_email_system_prompt(first_name)
                email_seq = claude.get_claude_sonnet35_response(
                    email_system_prompt, email_user_prompt
                )

                print(email_seq)

                cleaned_emails = self.extract_emails(email_seq)

                flattened = {
                    f"Subject {email['sequence']}": email["subject"]
                    for email in cleaned_emails
                }
                flattened.update(
                    {
                        f"Email Body {email['sequence']}": email["body"]
                        for email in cleaned_emails
                    }
                )

                emails_df = pd.DataFrame([flattened])
                emails_df["First Name"] = first_name
                emails_df["Last Name"] = last_name
                emails_df["LinkedIn URL"] = profile_url
                emails_dataframe.append(emails_df)

            except Exception as e:
                print(
                    f"Error generating email for {row.get('firstName', '')} {row.get('lastName', '')}: {e}"
                )
                continue

        if not emails_dataframe:
            return pd.DataFrame()  # Return empty if none succeeded

        all_emails = pd.concat(emails_dataframe, ignore_index=True)
        return all_emails

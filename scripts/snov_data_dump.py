"""
This script is used to dump the prospects data into Snov.io
"""

import sys
import os
import json
import requests
from ast import literal_eval

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.singleton import Singleton
from config.configuration_vars import ConfigVars


class Snov(metaclass=Singleton):
    """
    This class contains all the functions required to push data into Snov.io
    """

    def __init__(self):
        config = ConfigVars()
        self.client_id = literal_eval(config.snov_user_id)
        self.client_secret = literal_eval(config.snov_secret_key)

    def get_token(self):
        """
        This function is used to generate token
        """
        url = "https://api.snov.io/v1/oauth/access_token"
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    @staticmethod
    def headers(token):
        """
        Auth Function
        """
        return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    def add_prospect_to_list(
        self,
        email,
        full_name,
        first_name,
        last_name,
        country,
        linkedin_url,
        position,
        company_name,
        company_site,
        subject1,
        email1,
        subject2,
        email2,
        subject3,
        email3,
        subject4,
        email4,
        subject5,
        email5,
        answer1,
        answer2,
        answer3,
        answer4,
        answer5,
        answer6,
        answer7,
        answer8,
        answer9,
        answer10,
        answer11,
        answer12,
        answer13,
        answer14,
    ):
        """
        This is the main function that dumps the data into snov.io
        """
        token = self.get_token()
        params = {
            "access_token": token,
            "email": email,
            "fullName": full_name,
            "firstName": first_name,
            "lastName": last_name,
            "country": country,
            "socialLinks[linkedIn]": linkedin_url,
            "position": position,
            "companyName": company_name,
            "companySite": company_site,
            "updateContact": 1,
            "listId": "31453364",
            "customFields[Subject1]": subject1,
            "customFields[Email1]": email1,
            "customFields[Subject2]": subject2,
            "customFields[Email2]": email2,
            "customFields[Subject3]": subject3,
            "customFields[Email3]": email3,
            "customFields[Subject4]": subject4,
            "customFields[Email4]": email4,
            "customFields[Subject5]": subject5,
            "customFields[Email5]": email5,
            "customFields[What is the full legal name of the company?]": answer1,
            "customFields[What industry or niche do they primarily operate in?]": answer2,
            "customFields[Where is the company headquartered (city & country)?]": answer3,
            "customFields[What is the current estimated employee count?]": answer4,
            "customFields[What is the company website URL as mentioned in the LinkedIn Data?]": answer5,
            "customFields[Name of the individual]": answer6,
            "customFields[Their job title or designation]": answer7,
            "customFields[Are they likely a decision-maker (e.g., manager, VP, director, CXO)?]": answer8,
            "customFields[Are they hiring for roles that suggest growth, scaling, or specific operational challenges?]": answer9,
            "customFields[Based on the company's industry, employee size, and growth stage, does it align with the ICP?]": answer10,
            "customFields[Are they likely to have the budget and maturity to engage with our service/product?]": answer11,
            "customFields[Have they posted or reshared any content that shows their pain points or areas of focus?]": answer12,
            "customFields[Mention any known external tools or platforms the company uses.]": answer13,
            "customFields[Can you derive a clear value proposition we might be able to offer, based on their context?]": answer14,
        }

        res = requests.post("https://api.snov.io/v1/add-prospect-to-list", data=params)

        return json.loads(res.text)

    def dump_data_in_snov(self, final_data):
        """
        This function pushes data into Snov
        """
        for _, row in final_data[final_data["emails"].notna()].iterrows():
            email = row.get("emails", "")
            full_name = row.get("name", "")
            first_name = row.get("firstName", "")
            last_name = row.get("lastName", "")
            country = row.get("full_address", "")
            linkedin_url = row.get("profileURL", "")
            position = row.get("title", "")
            company_name = row.get("companyName", "")
            company_site = row.get("currentJob_site", "")

            # Email subjects and bodies
            subject1 = row.get("Subject 1", "")
            email1 = row.get("Email Body 1", "")
            subject2 = row.get("Subject 2", "")
            email2 = row.get("Email Body 2", "")
            subject3 = row.get("Subject 3", "")
            email3 = row.get("Email Body 3", "")
            subject4 = row.get("Subject 4", "")
            email4 = row.get("Email Body 4", "")
            subject5 = row.get("Subject 5", "")
            email5 = row.get("Email Body 5", "")

            # Questionnaire answers — default to "N/A" for better readability
            answer1 = row.get("What is the full legal name of the company?", "N/A")
            answer2 = row.get(
                "What industry or niche do they primarily operate in?", "N/A"
            )
            answer3 = row.get(
                "Where is the company headquartered (city & country)?", "N/A"
            )
            answer4 = row.get("What is the current estimated employee count?", "N/A")
            answer5 = row.get(
                "What is the company website URL as mentioned in the LinkedIn Data?",
                "N/A",
            )
            answer6 = row.get("Name of the individual", "N/A")
            answer7 = row.get("Their job title or designation", "N/A")
            answer8 = row.get(
                "Are they likely a decision-maker (e.g., manager, VP, director, CXO)?",
                "N/A",
            )
            answer9 = row.get(
                "Are they hiring for roles that suggest growth, scaling, or specific operational challenges? If yes, mention the roles.",
                "N/A",
            )
            answer10 = row.get(
                "Based on the company's industry, employee size, and growth stage, does it align with the Ideal Customer Profile (ICP) outlined in the ICP definition? Provide a brief rationale for your assessment.",
                "N/A",
            )
            answer11 = row.get(
                "Are they likely to have the budget and maturity to engage with our service/product?",
                "N/A",
            )
            answer12 = row.get(
                "Have they posted or reshared any content that shows their pain points or areas of focus? Summarize relevant content if available.",
                "N/A",
            )
            answer13 = row.get(
                "Mention any known external tools or platforms the company uses (e.g., CRMs, marketing automation, cloud platforms, AI tools).",
                "N/A",
            )
            answer14 = row.get(
                "Can you derive a clear value proposition we might be able to offer, based on their context?",
                "N/A",
            )

            _ = self.add_prospect_to_list(
                email,
                full_name,
                first_name,
                last_name,
                country,
                linkedin_url,
                position,
                company_name,
                company_site,
                subject1,
                email1,
                subject2,
                email2,
                subject3,
                email3,
                subject4,
                email4,
                subject5,
                email5,
                answer1,
                answer2,
                answer3,
                answer4,
                answer5,
                answer6,
                answer7,
                answer8,
                answer9,
                answer10,
                answer11,
                answer12,
                answer13,
                answer14,
            )

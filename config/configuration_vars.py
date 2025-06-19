"""
This script is used to store an instance of
all the variables that are secrets or hard-coded values.
"""

from ast import literal_eval
from config.configuration import Configuration
from config.singleton import Singleton


class ConfigVars(metaclass=Singleton):
    """
    Class to store all the secrets or hard-coded variables.
    """

    def __init__(self):
        configuration = Configuration()
        config = configuration.get_config()

        # Mongo
        self.mongo_uri = config["MONGO"]["MONGO_URI"]

        # Rapid API
        self.rapid_api_key = config["KEY"]["RAPID_API_KEY"]
        self.rapid_api_base_url = config["KEY"]["RAPID_API_BASE_URL"]

        # GHL
        self.ghl_api_key = config["GHL"]["API_KEY"]
        self.ghl_location_id = config["GHL"]["LOCATION_ID"]

        # SNOV
        self.snov_user_id = config["KEY"]["SNOV_APIUSERID"]
        self.snov_secret_key = config["KEY"]["SNOV_API_SECRET"]

        # LLM
        self.aws_secret_key = config["LLM"]["AWS_SECRET_KEY"]
        self.aws_access_key = config["LLM"]["AWS_ACCESS_KEY"]
        self.aws_region = config["LLM"]["AWS_REGION"]

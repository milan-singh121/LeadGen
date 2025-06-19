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
        # Get the configuration
        configuration = Configuration()
        config = configuration.get_config()

        # ===================== Mongo Credentials =====================#
        self.mongo_uri = config.get("MONGO", "MONGO_URI")

        # ===================== Secret Keys =====================#
        self.rapid_api_key = config.get("KEY", "RAPID_API_KEY")
        self.rapid_api_base_url = config.get("KEY", "RAPID_API_BASE_URL")

        # ===================== GHL Keys =====================#
        self.ghl_api_key = config.get("GHL", "API_KEY")
        self.ghl_location_id = config.get("GHL", "LOCATION_ID")

        # ===================== SNOV Keys =====================#
        self.snov_user_id = config.get("KEY", "SNOV_API_USERID")
        self.snov_secret_key = config.get("KEY", "SNOV_API_SECRET")

        # ===================== LLM Keys =====================#
        self.aws_secret_key = config.get("LLM", "AWS_SECRET_KEY")
        self.aws_access_key = config.get("LLM", "AWS_ACCESS_KEY")
        self.aws_region = config.get("LLM", "AWS_REGION")

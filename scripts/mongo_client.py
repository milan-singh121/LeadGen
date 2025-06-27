import sys
import os
import threading
from pymongo import MongoClient
from ast import literal_eval

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.singleton import Singleton
from config.configuration_vars import ConfigVars


class MongoDBClient(metaclass=Singleton):
    """
    Singleton MongoDB client for connecting to the LeadGen database.
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(MongoDBClient, cls).__new__(cls)
                    cls._instance._init_client()
        return cls._instance

    def _init_client(self):
        try:
            mongo_uri_raw = ConfigVars().mongo_uri
            if not mongo_uri_raw:
                raise ValueError("MONGO_URI is not set in ConfigVars.")

            MONGO_URI = literal_eval(mongo_uri_raw)
            if not MONGO_URI:
                raise ValueError("MONGO_URI evaluated to None or empty.")

            self.client = MongoClient(MONGO_URI, maxPoolSize=50, minPoolSize=10)
            self.db = self.client["LeadGen"]

        except Exception as e:
            raise RuntimeError(f"Failed to initialize MongoDB client: {e}")

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close_connection(self):
        if hasattr(self, "client"):
            self.client.close()

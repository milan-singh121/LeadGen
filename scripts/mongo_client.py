import sys
import os
import threading
from pymongo import MongoClient

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
        MONGO_URI = ConfigVars().mongo_uri
        if not MONGO_URI:
            raise ValueError("MONGO_URI is not set in the configuration script.")
        self.client = MongoClient(MONGO_URI, maxPoolSize=50, minPoolSize=10)
        self.db = self.client["LeadGen"]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close_connection(self):
        if hasattr(self, "client"):
            self.client.close()

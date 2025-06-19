import os
import sys
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from singleton import Singleton


class Config(metaclass=Singleton):
    def __init__(self):
        load_dotenv()
        self.__MONGO_CLIENT = MongoClient(
            os.environ.get("MONGO_URI"), server_api=ServerApi("1")
        )

    def get_db_client(self):
        return self.__MONGO_CLIENT

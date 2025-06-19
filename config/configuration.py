import os
import configparser
from config.singleton import Singleton


class Configuration(metaclass=Singleton):
    """
    Configuration Class
    """

    def __init__(self) -> None:
        self.config = None

    def get_config(self):
        """
        This function reads the config file stored in the directory
        """
        if not self.config:
            self.config = configparser.RawConfigParser()
            config_file_path = os.path.join(os.path.dirname(__file__), "config.txt")
            with open(config_file_path, encoding="UTF-8") as config_text:
                self.config.read_file(config_text)
        return self.config

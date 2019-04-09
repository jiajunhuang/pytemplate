import os


class Config:
    def __init__(self):
        self.SQLALCHEMY_DB_URI = os.getenv("SQLALCHEMY_DB_URI")
        self.SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO") == "True"
        self.CLOUDBUS_APP_ID = os.getenv("CLOUDBUS_APP_ID")
        self.CLOUDBUS_APP_SEC = os.getenv("CLOUDBUS_APP_SEC")
        self.CLOUDBUS_URL = os.getenv("CLOUDBUS_URL")
        self.DEBUG = os.getenv("DEBUG") == "True"


config = Config()

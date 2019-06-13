import os


class Config:
    def __init__(self):
        self.SQLALCHEMY_DB_URI = os.getenv("SQLALCHEMY_DB_URI", "sqlite:////data/db/tools.db")
        self.SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO") == "True"
        self.DEBUG = os.getenv("DEBUG") == "True"


config = Config()

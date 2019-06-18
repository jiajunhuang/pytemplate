import os


class Config:
    def __init__(self):
        self.SQLALCHEMY_DB_URI = os.getenv("SQLALCHEMY_DB_URI", "sqlite:////data/db/tools.db")
        self.SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO") == "True"
        self.DEBUG = os.getenv("DEBUG") == "True"
        self.SENTRY_DSN = os.getenv("SENTRY_DSN", "")

        # 配置，一般是全局变量
        self.FLASK_CONFIG = {
            "SITE_NAME": os.getenv("SITE_NAME", "Kindle Highlights/Notes Export"),
            "SITE_SLOGAN": os.getenv("SITE_SLOGAN", "Export your kindle highlights/notes"),
            "GA_CODE": os.getenv("GA_CODE"),  # Google Analytics Code
            "DISABLE_AD": os.getenv("DISABLE_AD") == "True",
        }


config = Config()

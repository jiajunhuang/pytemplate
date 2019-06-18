import logging

from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from loadbp import load_bp
from config import config

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
load_bp(app)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 最多传输1M笔记
# global variables
for k, v in config.FLASK_CONFIG.items():
    app.config[k] = v

if config.SENTRY_DSN:
    logging.info("integrating sentry...")
    sentry_sdk.init(
        dsn=config.SENTRY_DSN,
        integrations=[FlaskIntegration()]
    )


@app.route("/ping")
def ping():
    return "pong"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

import logging

from flask import Flask

from loadbp import load_bp

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
load_bp(app)


@app.route("/ping")
def ping():
    return "pong"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

import logging

from flask import Flask

from controllers.hello import hello_bp

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

app.register_blueprint(hello_bp)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

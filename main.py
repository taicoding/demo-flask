from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Hago un curso hare!"


if __name__ == "__main__":
    app.run(port=8080, debug=True)

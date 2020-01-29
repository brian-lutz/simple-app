from flask import Flask, Response
from sys import argv


app = Flask(__name__)


@app.route("/")
def index():
    return Response(status=200)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)


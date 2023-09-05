from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello Everyone"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")

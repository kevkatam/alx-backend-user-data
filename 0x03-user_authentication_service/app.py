#!/usr/bin/env python3
"""
simple flask app module
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def get_data() -> str:
    """ returns a JSON payload """
    data = {"message": "Bienvenue"}

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

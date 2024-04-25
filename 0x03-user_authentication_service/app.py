#!/usr/bin/env python3
"""
simple flask app module
"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def get_data() -> str:
    """ returns a JSON payload """
    data = {"message": "Bienvenue"}

    return jsonify(data)


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ registers a user and returns 400 status code"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

#!/usr/bin/env python3
"""
simple flask app module
"""
from flask import (
    Flask,
    jsonify,
    request,
    abort,
    make_response,
    redirect,
    url_for
)
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ implements login """
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        res = make_response(jsonify({"email": email, "message": "logged in"}))
        res.set_cookie('session_id', session_id)
        return res
    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ deletes the current user's session """
    session_id = request.cookies.get("session_id", None)
    user = AUTH.get_user_from_session_id(session_id)
    if user is None or session_id is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect(url_for('get_data'))


@app.route('/profile', strict_slashes=False)
def profile() -> str:
    """ gets existing user """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None or session_id is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ resets the token password of a particular user """
    email = request.form.get("email")
    if email is None:
        abort(403)
    reset_token = AUTH.get_reset_password_token(email)
    return jsonify({"email": email, "reset_token": reset_token}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

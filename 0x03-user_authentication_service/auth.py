#!/usr/bin/env python3
"""
 _hashed_password function module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ mehtod that takes in a password string arguments and return bytes """
    b_password = password.encode()
    hashed = bcrypt.hashpw(b_password, bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """ returns a string representation of uuid module """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ hashes user password and save user to database """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            new_user = self._db.add_user(email, hashed)
            return new_user
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """ check the user password if it mactches """
        try:
            user = self._db.find_user_by(email=email)
            b_password = password.encode()
            hashed_password = user.hashed_password
            if bcrypt.checkpw(b_password, hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ returns session ID """
        user = self._db.find_user_by(email=email)
        session_id = _generate_uuid()
        self._db

    def create_session(self, email: str) -> str:
        """ returns session ID """
        try:
            user = self._db.find_user_by(email=email)
            user_id = user.id
            session_id = _generate_uuid()
            self._db.update_user(user_id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ finds a user by session_id """
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ destroy user session """
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
            return None
        except NoResultFound:
            return None

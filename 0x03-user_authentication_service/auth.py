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
            b_password = password.encode('utf-8')
            hashed_password = user.hashed_password
            return bcrypt.checkpw(b_password, hashed_password)
        except NoResultFound:
            return False

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

    def get_reset_password_token(self, email: str) -> str:
        """ updaates user's reset_token database field """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError

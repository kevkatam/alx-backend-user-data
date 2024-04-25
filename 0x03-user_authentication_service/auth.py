#!/usr/bin/env python3
"""
 _hashed_password function module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ mehtod that takes in a password string arguments and return bytes """
    b_password = password.encode()
    hashed = bcrypt.hashpw(b_password, bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ hashes user password and save user to database """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError(f'User {email} already exists')

        hashed = _hashed_password(password)
        new_user = self._db.add_user(email, hashed)
        return new_user

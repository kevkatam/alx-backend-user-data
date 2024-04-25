#!/usr/bin/env python3
"""
 _hashed_password function module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ mehtod that takes in a password string arguments and return bytes """
    b_password = password.encode()
    hashed = bcrypt.hashpw(b_password, bcrypt.gensalt())
    return hashed

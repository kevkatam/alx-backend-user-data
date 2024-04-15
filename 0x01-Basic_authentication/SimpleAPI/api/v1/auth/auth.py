#!/usr/bin/env python3
"""
module for implementing authentication systems
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """ class template for all authetication system to implement """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ method that returns False """
        return False

    def authorization_header(self, request=None) -> str:
        """ method that returns None """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ method that returns None """
        return None

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
        if path is None or excluded_paths is None:
            return True
        i = "/api/v1/status"
        if path.endswith("*"):
            path = path[:-1]
        if path.endswith("/"):
            path = path[:-1]
        for excluded in excluded_paths:
            if excluded.endswith("*"):
                excluded = excluded[:-1]
            if excluded.endswith("/"):
                excluded = excluded[:-1]
            if path == i and i == excluded:
                return False
            if path == excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ method that returns None """
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ method that returns None """
        return None

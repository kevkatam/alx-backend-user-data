#!/usr/bin/env python3
"""
module containing basic_auth implementation
"""
from .auth import Auth


class BasicAuth(Auth):
    """ basic auth class """

    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """ returns Bae64 part of the authorization header for basic auth
        """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None

        a_header = authorization_header.split(' ')
        if a_header[0] != "Basic":
            return None
        return a_header[1]

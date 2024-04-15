#!/usr/bin/env python3
"""
module containing basic_auth implementation
"""
from .auth import Auth
from base64 import b64decode


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """ returns the decoded value of Base64 string """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None

        try:
            a_base64 = b64decode(base64_authorization_header)
        except Exception:
            return None
        return a_base64.decode('utf-8')

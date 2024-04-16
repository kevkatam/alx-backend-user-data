#!/usr/bin/env python3
"""
module containing basic_auth implementation
"""
from .auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


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
            a_base64 = base64_authorization_header.encode('utf-8')
            a_base64 = b64decode(a_base64)
            return a_base64.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """ returns user email and password from the Base64 decoded value """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        credentials = decoded_base64_authorization_header.split(':', 1)
        email, pwd = credentials
        return (credentials[0], credentials[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """ returns User instance based on email and password """
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None

        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User instance for a request """
        header = self.authorization_header(request)
        if header is not None:
            a_header = self.extract_base64_authorization_header(header)
            if a_header is not None:
                d_header = self.decode_base64_authorization_header(a_header)
                if d_header is not None:
                    email, pwd = self.extract_user_credentials(d_header)
                    if email is not None:
                        user = self.user_object_from_credentials(
                            email, pwd
                            )
                        return user
        return

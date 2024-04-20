#!/usr/bin/env python3
"""
Session authentication module
"""
from .auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ class for creating a new authentication mechanism """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a session id for user_id """
        if user_id is None or type(user_id) != str:
            return None

        self.session_id = str(uuid.uuid4())
        self.user_id_by_session_id[self.session_id] = user_id

        return self.session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns User ID based on a session ID """
        if session_id is None or type(session_id) != str:
            return None

        value = self.user_id_by_session_id.get(session_id)
        return value

    def current_user(self, request=None):
        """ returns User instance based on the cookie _my_session_id """
        session_id = self.session_cookie(request)
        if not session_id:
            return None

        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user

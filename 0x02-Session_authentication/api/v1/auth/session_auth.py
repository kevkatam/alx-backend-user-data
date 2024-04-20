#!/usr/bin/env python3
"""
Session authentication module
"""
from .auth import Auth
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

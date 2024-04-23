#!/usr/bin/env python3
"""
filter_datum module
"""
import logging
from typing import List
import re


def filter_datum(fields: List, redaction: str, msg: List, sep: str) -> str:
    """ returns the log messgae obfuscted"""
    for field in fields:
        msg = re.sub(field+'=.*?'+sep, field+'='+redaction+sep, msg)
    return msg

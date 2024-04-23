#!/usr/bin/env python3
"""
filter_datum module
"""
import logging
from typing import List
import re


def filter_datum(fields: List[str], red: str, msg: str, sep: str) -> str:
    """ returns the log messgae obfuscted"""
    for field in fields:
        msg = re.sub(field+'=.*?'+sep, field+'='+red+sep, msg)
    return msg

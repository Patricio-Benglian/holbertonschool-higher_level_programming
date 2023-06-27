#!/usr/bin/python3
"""
4-from_json_string module
"""
import json


def from_json_string(my_str):
    """
    returns python object from JSON string
    """
    return json.loads(my_str)

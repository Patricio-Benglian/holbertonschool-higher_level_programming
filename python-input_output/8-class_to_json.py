#!/usr/bin/python3
"""
8-class_to_json module
"""
import json


def class_to_json(obj):
    """
    returns object as JSON
    """
    return json.dumps(obj.__dict__)

#!/usr/bin/python3
"""
8-class_to_json module
"""


def class_to_json(obj):
    """
    returns object as JSON
    """
    return obj.__dict__

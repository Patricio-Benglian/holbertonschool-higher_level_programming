#!/usr/bin/python3
"""
inherits_from module
"""


def inherits_from(obj, a_class):
    """
    Returns true if obj is subclass of class
    """
    return isinstance(obj, a_class) if not type(obj) is a_class else False

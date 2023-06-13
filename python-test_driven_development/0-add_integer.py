#!/usr/bin/python3
"""
Add integers module
"""


def add_integer(a, b=98):
    """
    >>> add_integer(3, 5.5)
    8
    """
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    elif (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    else:
        return int(a)+int(b)

#!/usr/bin/python3
"""
2-append_write module
"""


def append_write(filename="", text=""):
    """
    appends to file
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)

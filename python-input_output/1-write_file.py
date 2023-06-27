#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    writes into file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)

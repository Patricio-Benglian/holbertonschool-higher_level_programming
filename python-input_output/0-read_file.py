#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    Reads file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        f.read()

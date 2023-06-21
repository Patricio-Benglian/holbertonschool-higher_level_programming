#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    Reads file
    """
    with open(filename) as f:
        f.read()

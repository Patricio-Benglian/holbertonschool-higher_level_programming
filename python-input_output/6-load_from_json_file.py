#!/usr/bin/python3
"""
6-load_from_json_file module
"""
import json


def load_from_json_file(filename):
    """
    loads object from JSON file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.loads(f)
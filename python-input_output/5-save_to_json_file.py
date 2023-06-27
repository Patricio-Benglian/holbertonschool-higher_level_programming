#!/usr/bin/python3
"""
5-save_to_json_file module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes Obj to text file using JSON representation
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))

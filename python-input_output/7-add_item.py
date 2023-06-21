#!/usr/bin/python3
"""
7-add_item module
"""
from sys import argv


saveJSON = __import__('5-save_to_json_file').save_to_json_file
loadJSON = __import__('6-load_from_json_file').load_from_json_file

try:
    listo = loadJSON("add_item.json")
except Exception:
    listo = []
saveJSON(listo + argv[1:], "add_item.json")

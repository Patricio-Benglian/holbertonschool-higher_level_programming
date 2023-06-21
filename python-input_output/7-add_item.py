#!/usr/bin/python3
"""
7-add_item module
"""
import json
from sys import argv


saveJSON = __import__('5-save_to_json_file').save_to_json_file
loadJSON = __import__('6-load_from_json_file').load_from_json_file

try:
    listo = loadJSON("add_item.json") + argv[1:]
except Exception:
    listo = argv[1:]
saveJSON(listo, "add_item.json")

#!/usr/bin/python3
"""
7-add_item module
"""
from sys import argv
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

listo = load_from_json_file("add_item.json") if path.isfile("add_item.json") else []
save_to_json_file(listo + argv[1:], "add_item.json")

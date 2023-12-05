#!/usr/bin/python3
"""Defining the save and load and sys modules."""

import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
try:
    pre_da = load_from_json_file(filename)
except Exception:
    pre_da = []

args = []
args = sys.argv[1:]
pre_da.extend(args)
save_to_json_file(pre_da, filename)

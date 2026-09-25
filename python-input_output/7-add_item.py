#!/usr/bin/python3
"""
Script that adds all command line arguments to a list and saves them to a JSON file.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_target = "add_item.json"

try:
    items_list = load_from_json_file(file_target)
except FileNotFoundError:
    items_list = []

items_list.extend(sys.argv[1:])
save_to_json_file(items_list, file_target)

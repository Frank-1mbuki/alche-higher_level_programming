#!/usr/bin/python3
"""
Module containing the load_from_json_file function.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python Object from a JSON file.
    """
    with open(filename, encoding="utf-8") as file_handle:
        return json.load(file_handle)

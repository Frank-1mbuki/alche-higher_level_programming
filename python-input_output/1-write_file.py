#!/usr/bin/python3
"""
Module containing the write_file function.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns character count.
    """
    with open(filename, mode="w", encoding="utf-8") as file_handle:
        return file_handle.write(text)

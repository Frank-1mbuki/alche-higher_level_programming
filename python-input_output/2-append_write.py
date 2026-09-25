#!/usr/bin/python3
"""
Module containing the append_write function.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns character count.
    """
    with open(filename, mode="a", encoding="utf-8") as file_handle:
        return file_handle.write(text)

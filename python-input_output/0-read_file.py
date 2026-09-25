#!/usr/bin/python3
"""
Module containing the read_file function.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to standard output.
    """
    with open(filename, encoding="utf-8") as file_handle:
        print(file_handle.read(), end="")

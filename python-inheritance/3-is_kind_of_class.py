#!/usr/bin/python3
"""
Module providing an instance or inherited instance checking function.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance or inherited instance of a_class.
    """
    return isinstance(obj, a_class)

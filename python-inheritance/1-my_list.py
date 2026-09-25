#!/usr/bin/python3
"""
Module defining a class MyList that inherits from list.
"""


class MyList(list):
    """
    Custom list class that includes sorted printing capabilities.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        """
        print(sorted(self))

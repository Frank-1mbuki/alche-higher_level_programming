#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute.
"""


class Square:
    """
    Defines a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square (no type/value verification yet).
        """
        self.__size = size

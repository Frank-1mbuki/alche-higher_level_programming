#!/usr/bin/python3
"""
This module defines a Square class with size type and value validation.
"""


class Square:
    """
    Defines a square with a validated private size attribute.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square, defaults to 0.

        Raises:
            TypeError: If size is not an integer (and not a boolean subclass).
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

#!/usr/bin/python3
"""
Module defining a Square class inheriting from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a square using Rectangle initialization.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a validated size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

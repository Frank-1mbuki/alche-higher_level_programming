#!/usr/bin/python3
"""
Module defining a Square class with custom string representation.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a square with area calculation and custom string display.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a validated size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns the formatted string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"

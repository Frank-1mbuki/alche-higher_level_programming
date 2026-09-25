#!/usr/bin/python3
"""
Module defining a Rectangle class with area calculation and string display.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a rectangle with width, height, area, and custom string display.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with validated dimensions.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the formatted string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

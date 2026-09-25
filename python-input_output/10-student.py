#!/usr/bin/python3
"""
Module defining the Student class with attribute filtering.
"""


class Student:
    """
    Defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance, filtering attributes if requested.
        """
        if isinstance(attrs, list) and all(isinstance(element, str) for element in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__

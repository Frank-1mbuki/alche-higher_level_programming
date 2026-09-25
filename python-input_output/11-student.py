#!/usr/bin/python3
"""
Module defining the Student class with serialization and reloading capabilities.
"""


class Student:
    """
    Defines a student with json serialization and deserialization methods.
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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.
        """
        for attr_key, attr_val in json.items():
            setattr(self, attr_key, attr_val)

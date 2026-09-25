#!/usr/bin/python3
"""
Generates all task files for the python-input_output project.
"""
import os

files = {
    "0-read_file.py": """#!/usr/bin/python3
\"\"\"
Module containing the read_file function.
\"\"\"


def read_file(filename=""):
    \"\"\"
    Reads a text file (UTF8) and prints its contents to standard output.
    \"\"\"
    with open(filename, encoding="utf-8") as file_handle:
        print(file_handle.read(), end="")
""",

    "1-write_file.py": """#!/usr/bin/python3
\"\"\"
Module containing the write_file function.
\"\"\"


def write_file(filename="", text=""):
    \"\"\"
    Writes a string to a text file (UTF8) and returns character count.
    \"\"\"
    with open(filename, mode="w", encoding="utf-8") as file_handle:
        return file_handle.write(text)
""",

    "2-append_write.py": """#!/usr/bin/python3
\"\"\"
Module containing the append_write function.
\"\"\"


def append_write(filename="", text=""):
    \"\"\"
    Appends a string to the end of a text file (UTF8) and returns character count.
    \"\"\"
    with open(filename, mode="a", encoding="utf-8") as file_handle:
        return file_handle.write(text)
""",

    "3-to_json_string.py": """#!/usr/bin/python3
\"\"\"
Module containing the to_json_string function.
\"\"\"
import json


def to_json_string(my_obj):
    \"\"\"
    Returns the JSON representation of an object as a string.
    \"\"\"
    return json.dumps(my_obj)
""",

    "4-from_json_string.py": """#!/usr/bin/python3
\"\"\"
Module containing the from_json_string function.
\"\"\"
import json


def from_json_string(my_str):
    \"\"\"
    Returns a Python object represented by a JSON string.
    \"\"\"
    return json.loads(my_str)
""",

    "5-save_to_json_file.py": """#!/usr/bin/python3
\"\"\"
Module containing the save_to_json_file function.
\"\"\"
import json


def save_to_json_file(my_obj, filename):
    \"\"\"
    Writes an Object to a text file using a JSON representation.
    \"\"\"
    with open(filename, mode="w", encoding="utf-8") as file_handle:
        json.dump(my_obj, file_handle)
""",

    "6-load_from_json_file.py": """#!/usr/bin/python3
\"\"\"
Module containing the load_from_json_file function.
\"\"\"
import json


def load_from_json_file(filename):
    \"\"\"
    Creates a Python Object from a JSON file.
    \"\"\"
    with open(filename, encoding="utf-8") as file_handle:
        return json.load(file_handle)
""",

    "7-add_item.py": """#!/usr/bin/python3
\"\"\"
Script that adds all command line arguments to a list and saves them to a JSON file.
\"\"\"
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_target = "add_item.json"

try:
    items_list = load_from_json_file(file_target)
except FileNotFoundError:
    items_list = []

items_list.extend(sys.argv[1:])
save_to_json_file(items_list, file_target)
""",

    "8-class_to_json.py": """#!/usr/bin/python3
\"\"\"
Module containing the class_to_json function.
\"\"\"


def class_to_json(obj):
    \"\"\"
    Returns the dictionary description with simple data structure for JSON serialization.
    \"\"\"
    return obj.__dict__
""",

    "9-student.py": """#!/usr/bin/python3
\"\"\"
Module defining the Student class.
\"\"\"


class Student:
    \"\"\"
    Defines a student by first name, last name, and age.
    \"\"\"

    def __init__(self, first_name, last_name, age):
        \"\"\"
        Initializes a Student instance.
        \"\"\"
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        \"\"\"
        Retrieves a dictionary representation of a Student instance.
        \"\"\"
        return self.__dict__
""",

    "10-student.py": """#!/usr/bin/python3
\"\"\"
Module defining the Student class with attribute filtering.
\"\"\"


class Student:
    \"\"\"
    Defines a student by first name, last name, and age.
    \"\"\"

    def __init__(self, first_name, last_name, age):
        \"\"\"
        Initializes a Student instance.
        \"\"\"
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        \"\"\"
        Retrieves a dictionary representation of a Student instance, filtering attributes if requested.
        \"\"\"
        if isinstance(attrs, list) and all(isinstance(element, str) for element in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__
""",

    "11-student.py": """#!/usr/bin/python3
\"\"\"
Module defining the Student class with serialization and reloading capabilities.
\"\"\"


class Student:
    \"\"\"
    Defines a student with json serialization and deserialization methods.
    \"\"\"

    def __init__(self, first_name, last_name, age):
        \"\"\"
        Initializes a Student instance.
        \"\"\"
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        \"\"\"
        Retrieves a dictionary representation of a Student instance, filtering attributes if requested.
        \"\"\"
        if isinstance(attrs, list) and all(isinstance(element, str) for element in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        \"\"\"
        Replaces all attributes of the Student instance using a dictionary.
        \"\"\"
        for attr_key, attr_val in json.items():
            setattr(self, attr_key, attr_val)
""",

    "12-pascal_triangle.py": """#!/usr/bin/python3
\"\"\"
Module containing the pascal_triangle function.
\"\"\"


def pascal_triangle(n):
    \"\"\"
    Returns a list of lists of integers representing Pascal's triangle of n.
    \"\"\"
    if n <= 0:
        return []

    triangle = [[1]]
    for row_idx in range(1, n):
        previous_row = triangle[-1]
        current_row = [1]
        for col_idx in range(1, row_idx):
            current_row.append(previous_row[col_idx - 1] + previous_row[col_idx])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
"""
}

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

    os.chmod(filename, 0o755)
    print(f"Successfully generated: {filename}")

print("\nAll input/output task files created successfully!")

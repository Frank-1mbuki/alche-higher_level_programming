#!/usr/bin/python3
"""
Generates all task files and test files for the python-inheritance project.
"""
import os

# Ensure the tests directory exists
os.makedirs("tests", exist_ok=True)

files = {
    "0-lookup.py": """#!/usr/bin/python3
\"\"\"
Module providing a function to retrieve available attributes and methods.
\"\"\"


def lookup(obj):
    \"\"\"
    Returns the list of available attributes and methods of an object.
    \"\"\"
    return dir(obj)
""",

    "1-my_list.py": """#!/usr/bin/python3
\"\"\"
Module defining a class MyList that inherits from list.
\"\"\"


class MyList(list):
    \"\"\"
    Custom list class that includes sorted printing capabilities.
    \"\"\"

    def print_sorted(self):
        \"\"\"
        Prints the elements of the list in ascending sorted order.
        \"\"\"
        print(sorted(self))
""",

    "tests/1-my_list.txt": """===========================
Tests for MyList Class
===========================

Setup:
    >>> MyList = __import__('1-my_list').MyList

Normal operations:
    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)
    >>> print(my_list)
    [1, 4, 2, 3, 5]
    >>> my_list.print_sorted()
    [1, 2, 3, 4, 5]
    >>> print(my_list)
    [1, 4, 2, 3, 5]

Unsorted / Negative numbers:
    >>> my_list2 = MyList([-1, -10, 5, 0])
    >>> my_list2.print_sorted()
    [-10, -1, 0, 5]

Empty list:
    >>> empty_list = MyList()
    >>> empty_list.print_sorted()
    []
""",

    "2-is_same_class.py": """#!/usr/bin/python3
\"\"\"
Module providing an exact instance checking function.
\"\"\"


def is_same_class(obj, a_class):
    \"\"\"
    Returns True if obj is exactly an instance of a_class, else False.
    \"\"\"
    return type(obj) is a_class
""",

    "3-is_kind_of_class.py": """#!/usr/bin/python3
\"\"\"
Module providing an instance or inherited instance checking function.
\"\"\"


def is_kind_of_class(obj, a_class):
    \"\"\"
    Returns True if obj is an instance or inherited instance of a_class.
    \"\"\"
    return isinstance(obj, a_class)
""",

    "4-inherits_from.py": """#!/usr/bin/python3
\"\"\"
Module providing a subclass instance checking function.
\"\"\"


def inherits_from(obj, a_class):
    \"\"\"
    Returns True if obj is an instance of a subclass of a_class.
    \"\"\"
    return issubclass(type(obj), a_class) and type(obj) is not a_class
""",

    "5-base_geometry.py": """#!/usr/bin/python3
\"\"\"
Module defining an empty BaseGeometry class.
\"\"\"


class BaseGeometry:
    \"\"\"
    An empty base geometry class.
    \"\"\"
    pass
""",

    "6-base_geometry.py": """#!/usr/bin/python3
\"\"\"
Module defining a BaseGeometry class with an area method stub.
\"\"\"


class BaseGeometry:
    \"\"\"
    Base geometry class that defines geometry operation interfaces.
    \"\"\"

    def area(self):
        \"\"\"
        Raises an Exception indicating area is not implemented.
        \"\"\"
        raise Exception("area() is not implemented")
""",

    "7-base_geometry.py": """#!/usr/bin/python3
\"\"\"
Module defining BaseGeometry with area calculation and integer validation.
\"\"\"


class BaseGeometry:
    \"\"\"
    Base geometry class providing attribute validation and method interfaces.
    \"\"\"

    def area(self):
        \"\"\"
        Raises an Exception indicating area is not implemented.
        \"\"\"
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        \"\"\"
        Validates that value is an integer strictly greater than 0.
        \"\"\"
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
""",

    "tests/7-base_geometry.txt": """===========================
Tests for BaseGeometry Class
===========================

Setup:
    >>> BaseGeometry = __import__('7-base_geometry').BaseGeometry
    >>> bg = BaseGeometry()

Valid integer validation:
    >>> bg.integer_validator("my_int", 12)
    >>> bg.integer_validator("width", 89)

Type error cases:
    >>> bg.integer_validator("name", "John")
    Traceback (most recent call last):
        ...
    TypeError: name must be an integer

    >>> bg.integer_validator("flag", True)
    Traceback (most recent call last):
        ...
    TypeError: flag must be an integer

Value error cases:
    >>> bg.integer_validator("age", 0)
    Traceback (most recent call last):
        ...
    ValueError: age must be greater than 0

    >>> bg.integer_validator("distance", -4)
    Traceback (most recent call last):
        ...
    ValueError: distance must be greater than 0

Area method test:
    >>> bg.area()
    Traceback (most recent call last):
        ...
    Exception: area() is not implemented
""",

    "8-rectangle.py": """#!/usr/bin/python3
\"\"\"
Module defining a Rectangle class inheriting from BaseGeometry.
\"\"\"
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    \"\"\"
    Defines a rectangle using BaseGeometry validation.
    \"\"\"

    def __init__(self, width, height):
        \"\"\"
        Initializes a Rectangle instance with validated width and height.
        \"\"\"
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
""",

    "9-rectangle.py": """#!/usr/bin/python3
\"\"\"
Module defining a Rectangle class with area calculation and string display.
\"\"\"
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    \"\"\"
    Defines a rectangle with width, height, area, and custom string display.
    \"\"\"

    def __init__(self, width, height):
        \"\"\"
        Initializes a Rectangle instance with validated dimensions.
        \"\"\"
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        \"\"\"
        Calculates and returns the area of the rectangle.
        \"\"\"
        return self.__width * self.__height

    def __str__(self):
        \"\"\"
        Returns the formatted string representation of the rectangle.
        \"\"\"
        return f"[Rectangle] {self.__width}/{self.__height}"
""",

    "10-square.py": """#!/usr/bin/python3
\"\"\"
Module defining a Square class inheriting from Rectangle.
\"\"\"
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    \"\"\"
    Defines a square using Rectangle initialization.
    \"\"\"

    def __init__(self, size):
        \"\"\"
        Initializes a Square instance with a validated size.
        \"\"\"
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
""",

    "11-square.py": """#!/usr/bin/python3
\"\"\"
Module defining a Square class with custom string representation.
\"\"\"
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    \"\"\"
    Defines a square with area calculation and custom string display.
    \"\"\"

    def __init__(self, size):
        \"\"\"
        Initializes a Square instance with a validated size.
        \"\"\"
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        \"\"\"
        Returns the formatted string representation of the square.
        \"\"\"
        return f"[Square] {self.__size}/{self.__size}"
"""
}

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

    if filename.endswith(".py"):
        os.chmod(filename, 0o755)

    print(f"Successfully generated: {filename}")

print("\nAll inheritance project files created!")

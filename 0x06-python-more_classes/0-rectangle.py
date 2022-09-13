#!/usr/bin/python3
"""
    Creating a class with conditions and errors raised when applicable
"""


class Rectangle:
    """Creating a class for the rectangle"""
    def __init__(self, width=0, height=0):
        """Instantation to create objects"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

#!/usr/bin/python3
"""
    Creating a class with conditions and errors raised when applicable
"""


class Rectangle:
    """Creating a class for the rectangle"""
    def __init__(self, width=0, height=0):
        """Instantation to create objects"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
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
        elif value < 0:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

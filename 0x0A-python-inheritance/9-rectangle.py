#!/usr/bin/python3
"""
    Writing an empty class
"""


class BaseGeometry:
    """New class"""
    def area(self):
        """Area for BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating the value"""
        if type(value)is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""
    New class for rectangles.
"""


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instatiation for width and height)"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area will be overriden by the parent area function in inheritance"""
        return self.__width * self.__height

    def __str__(self):
        """Returning the rectangle description"""
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string

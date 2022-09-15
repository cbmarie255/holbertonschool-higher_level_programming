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

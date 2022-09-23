#!/usr/bin/python3
"""
    Building a square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherited from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Super classing variables for the square from rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        message = "[Square] ({}) ".format(self.id, end='')
        message2 = "{}/{} - ".format(self.x, self.y, end='')
        message3 = "{}".format(self.width)
        return message + message2 + message3

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

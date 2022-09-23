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

    def update(self, *args, **kwargs):
        """assigning attibutes"""
        if args is not None and len(args) > 0:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.size = arg
                if count == 2:
                    self.x = arg
                if count == 3:
                    self.y = arg
                count = count + 1
        else: 
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

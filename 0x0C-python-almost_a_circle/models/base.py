#!/usr/bin/python3
"""
    Creating the first class, Base.
"""


class Base:
    """defining the first class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """declaring class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

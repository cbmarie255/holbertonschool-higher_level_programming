#!/usr/bin/python3
"""
    Creating the first class, Base.
"""
import json


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

    def to_json_string(list_dictionaries):
        """changing json to string"""
        if list_dictionaries is None or len(list_dictionaries) < 0:
            list_dictionaries = []
            return list_dictionaries
        else:
            return json.dumps(list_dictionaries)

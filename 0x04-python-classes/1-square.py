#!/usr/bin/python3

"""Defining class Square with conditions"""

class Square:
    """defining the class named Square"""
    def __init__(self, size=0):
        """Initializing the size of the square"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

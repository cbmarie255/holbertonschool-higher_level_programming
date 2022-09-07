#!/usr/bin/python3

"""Defining class Square with conditions and a public instance method"""


class Square:
    """defining a class named Square"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    
    def area (self):
        """will return the current square area"""
        squared = self.__size**2
        return squared

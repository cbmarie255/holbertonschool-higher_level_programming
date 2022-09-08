#!/usr/bin/python3

"""Adding a getter and setter to the square"""


class Square:
    """defining the class named Square"""
    def __init__(self, size=0):
        """Initializing the size of the square"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """to retrieve the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """will return the current square area"""
        squared = self.__size**2
        return squared

    def my_print(self):
        if self.__size == 0:
            print("")
        for row in range(self.__size):
            for column in range(self.__size):
                print("#", end='')
            print("")

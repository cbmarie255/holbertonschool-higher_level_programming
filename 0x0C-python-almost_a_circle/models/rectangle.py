#!/usr/bin/python3
"""
    Writing a class that inherits from Base.
"""


from models.base import Base


class Rectangle(Base):
    """Inherited class that attributes to rectangles"""

    @property
    def width(self):
        """getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor and initiation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints the Rectangle instance with #"""
        for y_axis in range(0, self.__y):
            print()
        for column in range(0, self.__height):
            string = ''
            for x_axis in range(0, self.__x):
                string = string + ' '
            for row in range(0, self.__width):
                string = string + '#'
            print(string)

    def __str__(self):
        """Using str method to return a message"""
        message = "[Rectangle] ({}) ".format(self.id, end='')
        message2 = "{}/{} ".format(self.x, self.y, end='')
        message3 = "- {}/{}".format(self.width, self.height)
        return message + message2 + message3

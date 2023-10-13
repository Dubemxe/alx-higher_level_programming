#!/usr/bin/python3
'''Defines a class Rectangle inherited from Base'''
from models.base import Base

class Rectangle(Base):
    '''Represent a Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes a new Rectangle'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Get the width of Rectangle'''
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must > 0")
        self.__width = value

    @property
    def height(self):
        '''Get the height of Rectangle'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must > 0")
        self.__height = value

    @property
    def x(self):
        '''Get the x  coordinate of Rectangle'''
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Get the y coordinate of Rectangle'''
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Get the area of Rectangle'''
        return (self.__height * self.__width)

    def display(self):
        '''Represent Rectangle with ``#`` character'''
        if self.width == 0 or self.height == 0:
            return ("")

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

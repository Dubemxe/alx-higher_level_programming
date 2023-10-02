#!/usr/bin/python3
'''Define a class Rectangle wit width and height'''


class Rectangle:
    '''Represents a rectangle'''

    def __init__(self, width=0, height=0):
        '''Returns the width and height of rectangle
        raise:
            TypeError: if width and height is non-integer or < 0'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Get the current width of the Rectangle'''
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Get the current height of the rectangle'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Get the area of the rectangle'''
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
           return (0)
        return ((self.__width * 2) + (self.__height * 2))

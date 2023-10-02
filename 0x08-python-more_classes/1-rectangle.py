#!/usr/bin/python3
'''Define a class Rectangle wit width and height'''


class Rectangle:
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

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
        self.__width = value

    @property
    def height(self):
        '''Get the height of Rectangle'''
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''Get the x  coordinate of Rectangle'''
        return (self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        '''Get the y coordinate of Rectangle'''
        return (self.__y)

    @y.setter
    def y(self, value):
        self.__y = value

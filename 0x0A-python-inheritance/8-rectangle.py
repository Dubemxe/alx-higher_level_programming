#!/usr/bin/python3
'''Defines a class Rectangle that inherits from BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Reprents a rectangle'''

    def __init__(self, width, height):
        '''Initialize a new triangle

        Args:
            width - the width of the new rectangle
            height - the height of the new rectangle'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

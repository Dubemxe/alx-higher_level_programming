#!/usr/bin/python3
'''Define a square'''


class Square:
    '''A square class'''
    def __init__(self, size=0):
        '''checks for Errors and raise an exception
        and return the area of size'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''return the current square area'''
        return (self.__size * self.__size)

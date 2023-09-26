#!/usr/bin/python3
'''Define a square with size'''


class Square:
    '''A square class'''
    def __init__(self, size=0):
        '''Raise Exceptions when size is not an integer or < 0'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

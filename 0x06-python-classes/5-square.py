#!/usr/bin/python3
'''Definhe a square'''


class Square:
    '''A square class'''
    def __init__(self, size=0):
        '''A square with property and setter which
        returns the squatre area'''
        self.size = size

    @property
    def size(self):
        '''Get the current square size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''size setter'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        '''prints the square bwith the character #'''
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

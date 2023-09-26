#!/usr/bin/python3
'''Define a square class'''


class Square:
    '''A square class'''
    def __init__(self, size=0):
        '''Initialize a new square'''
        self.size = size

    @property
    def size(self):
        '''Get the current size of the square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''return the current area of the square'''
        return (self.__size * self.__size)

    def __eq__(self, other):
        '''the ==  comparision of a square'''
        return self.area() == other.area()

    def __ne__(self, other):
        """ the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        '''the < comparison to a Square'''
        return self.area() < other.area()

    def __le__(self, other):
        '''the <= comparison to a Square'''
        return self.area() <= other.area()

    def __gt__(self, other):
        '''the > comparison to a Square'''
        return self.area() > other.area()

    def __ge__(self, other):
        '''the >= compmarison to a Square'''
        return self.area() >= other.area()

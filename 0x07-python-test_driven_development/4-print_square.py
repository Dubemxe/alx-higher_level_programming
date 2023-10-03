#!/usr/bin/python3
'''Define a function print_sqaure'''
def print_square(size):
    '''Prints a square with te "#" character

    Args:
        size: the length of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if if size is less than 0
        TypeError: if size is a float and is less than 0
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

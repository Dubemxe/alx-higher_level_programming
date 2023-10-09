#!/usr/bin/python3
'''Defines a class-checking function'''


def is_same_class(obj, a_class):
    '''Check if the object is exactly an instance of the specified class

    Args:
        obj - The object to check
        a_class - the class to match the type of obj with.
    Return:
        True if they match, else Return false'''
    if type(obj) == a_class:
        return True
    return False

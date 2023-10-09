#!/usr/bin/python3
'''Defines a inheritance checking function'''


def inherits_from(obj, a_class):
    '''check if the object is inherited from the class

    Args:
        obj - the object to check
        a_class - the type to match obj with
    Return:
        True if the match, or return False'''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

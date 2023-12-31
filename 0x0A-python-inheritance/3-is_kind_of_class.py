#!/usr/bin/python3
'''Define a class and inherited class-checking function'''


def is_kind_of_class(obj, a_class):
    '''Check if the object is an instance or inherited instance of a class

    Args:
        obj - object to check
        a_class - the class to match the type of obj with
    Return:
        True if the match, else return False'''
    if isinstance(obj, a_class):
        return True
    return False

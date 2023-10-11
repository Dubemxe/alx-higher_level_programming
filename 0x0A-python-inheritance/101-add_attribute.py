#!/usr/bin/python3
'''Defines a function that adds attributes to objects'''


def add_attribute(obj, attr, value):
    '''Add a new attribute to the object

    Args:
        obj - object where attr is added
        attr - attribute to be added to obj
        value - the value of attr'''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

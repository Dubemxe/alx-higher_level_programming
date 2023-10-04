#!/usr/bin/python3
'''Define a say_my_name function'''


def say_my_name(first_name, last_name=""):
    '''Prints My name is <first_name> <last_name>

    Args:
        first_name: first name provided
        last_name: second name provided
    Raise:
        TypeError: if first_name and last_name are non-strings
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

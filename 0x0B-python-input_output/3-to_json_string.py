#!/usr/bin/python3
'''Defines a function that returns a JSON representation of an Object'''
import json


def to_json_string(my_obj):
    '''Represent the object in JSON

    Args:
        my_obj(str) - the object to JSONify
    Return:
        the JSON represntation of my_obj'''
    return json.dumps(my_obj)

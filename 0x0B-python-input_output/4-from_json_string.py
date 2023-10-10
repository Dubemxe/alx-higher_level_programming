#!/usr/bin/python3
'''Defines a JSON-to-object function'''
import json


def from_json_string(my_str):
    '''Represent a JSON string as a python object'''
    return json.loads(my_str)

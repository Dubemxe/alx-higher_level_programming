#!/usr/bin/python3
'''Defines a JSON file-writing function'''
import json


def save_to_json_file(my_obj, filename):
    '''write an object to a text file using JSON presentation'''
    with open(filename, mode="w") as txt:
        json.dump(my_obj, txt)

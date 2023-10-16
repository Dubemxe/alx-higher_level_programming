#!/usr/bin/python3
'''Defines a class Base'''
import json


class Base:
    '''Get the base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Assign the public instance attribute id with this argument value

        Otherwise - increment __nb_objects and assign the new value to the
        public instance attribute id
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Return the JSON string represenntation of a dictionary'''
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        '''Save a JSON string to a file'''
        if list_objs is None:
            list_objs = []
        filename = cls.__name__  + '.json'

        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(filename, 'w') as jsonfile:
            jsonfile.write(json_string)

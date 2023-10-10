#!/usr/bin/python3
'''Defines a class Student'''


class Student:
    '''Represent a student'''
    def __init__(self, first_name, last_name, age):
        '''Initialize a new student

        Args:
            first_name - first name of Student
            last_name - last name of Student
            age - age of Student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieve a dictionary representation of Student
            If attrs is a list of strings, represents only those attributes
        included in the list'''
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        '''Replace all attributes of Student'''
        for i, j in json.items():
            setattr(self, i, j)

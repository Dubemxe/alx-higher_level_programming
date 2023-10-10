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

    def to_json(self):
        '''Retrieve a dictionary representation of Student'''
        return self.__dict__

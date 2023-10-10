#!/usr/bin/python3
'''Defines a file reading function'''


def read_file(filename="my_file_0.txt"):
    '''Open a file with the read-only permission'''
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())

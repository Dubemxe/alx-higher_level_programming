#!/usr/bin/python3
'''Defines a file reading function'''


def read_file(filename=""):
    '''Open a file with the read-only permission'''
    with open(filename, encoding="utf-8") as my_file:
        for line in my_file:
            print(line, end="")

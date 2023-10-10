#!/usr/bin/python3
'''Defines a write to file function'''


def write_file(filename="", text=""):
    '''Write a string to a file

    Args:
        filename - file to write in
        text - string to wite in filename
    Return:
        the number of characters written'''
    count = 0
    with open(filename, mode="w", encoding="utf-8") as my_file:
        count = my_file.write(text)
    return count

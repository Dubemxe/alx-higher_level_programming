#!/usr/bin/python3
'''Defines a append to end of file function'''


def append_write(filename="", text=""):
    '''Append a string to the end a file

    Args:
        filename - file to write in
        text - string to append to  filename
    Return:
        the number of characters appended'''
    count = 0
    with open(filename, mode="a", encoding="utf-8") as my_file:
        count = my_file.write(text)
    return count

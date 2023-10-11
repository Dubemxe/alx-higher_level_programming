#!/usr/bin/python3
'''Defines a text file insertion function'''


def append_after(filename="", search_string="", new_string=""):
    '''Insert text to a file, after each line containing a specific string'''
    txt = ""
    with open(filename) as reader:
        for line in reader:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as insert:
        insert.write(txt)

#!/usr/bin/python3
'''Define an object attribute and method lookup function'''


def lookup(obj):
    '''return a list of available attributes and methods'''
    return dir(obj)

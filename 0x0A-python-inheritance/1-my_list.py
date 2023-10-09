#!/usr/bin/python3
'''Defines an inherited class MyList'''


class MyList(list):
    '''Sorted printing for bult-in list class'''
    def print_sorted(self):
        '''Print the list in acesending sorted order'''
        print(sorted(self))

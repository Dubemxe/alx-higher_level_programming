#!/usr/bin/python3
'''Defines a class MyInt that inherites from Int'''


class MyInt(int):
    '''invert int operators ``==`` and ``!=``'''
    def __eq__(self, value):
        '''Reinvert ``==``  to ``!=`` operator'''
        return self.real != value

    def __ne__(self, value):
        '''Reinvert ``!=``  to ``==`` operator'''
        return self.real == value

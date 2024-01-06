#!/usr/bin/python3
"""Defines a Function that finds the peak in an unsorted list"""


def find_peak(list_of_integers):
    """Finds the peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]

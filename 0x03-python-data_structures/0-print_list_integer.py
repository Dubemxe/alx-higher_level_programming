#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list:
        for item in my_list:
            item = int(item)
        for i in range(1):
            print("{}".format(item))

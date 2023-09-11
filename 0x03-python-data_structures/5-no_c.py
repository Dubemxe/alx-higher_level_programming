#!/usr/bin/python3
def no_c(my_string):
    the_c = "cC"
    result = ""
    for char in my_string:
        if char not in the_c:
            result += char

    return result

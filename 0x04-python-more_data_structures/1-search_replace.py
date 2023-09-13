#!/usr/bin/python3
def search_replace(my_list, search, replace):
    #  replaces all occurrences of an element by another in a new list

    new_List = []
    for item in my_list:
        if item == search:
            new_List.append(replace)
        else:
            new_List.append(item)

    return (new_List)

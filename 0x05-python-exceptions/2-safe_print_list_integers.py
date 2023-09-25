#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for ele in my_list:
            if isinstance(ele, int):
                print("{:d}".format(ele), end="")
                count += 1
                if count >= x:
                    break
    except IndexError as e:
        print(e)
        raise IndexError("list index out of range")
    finally:
        print()
    return count

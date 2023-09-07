#!/usr/bin/python3

if __name__ == "__main__":
    import sys
# get number of arguments
num_args = len(sys.argv) - 1

if num_args == 0:
    print("0 arguments.")

elif num_args == 1:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(num_args))
# print the list
    for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

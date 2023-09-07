#!/usr/bin/python3

for i in range(ord('a'), ord('z') + 1):
    i = chr(i)
    if (i) not in ('q', 'e'):
        print("{}".format(i), end='')

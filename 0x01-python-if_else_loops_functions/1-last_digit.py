#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

# convert the number to string
num_2_str = str(number)

ld = int(num_2_str[-1])
ld *= -1 if number < 0 else 1

if (ld > 5 and number > 0):
    print("Last digit of {} is {} and is greater than 5".format(number, ld))
if (ld == 0 and number > 0):
    print("Last digit of {} is {} and is 0".format(number, ld))
if (ld < 6 and ld != 0):
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,ld))

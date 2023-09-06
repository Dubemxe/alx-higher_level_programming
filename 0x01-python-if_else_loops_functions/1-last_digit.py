#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

# convert the number to string
num_2_str = str(number)

last_digit = int(num_2_str[-1])

if (last_digit > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit))

if (last_digit == 0):
    print("Last digit of {} is {} and is 0".format(number, last_digit))

if (last_digit < 6 and last_digit != 0):
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))

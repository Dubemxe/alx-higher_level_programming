#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
a = 10
b = 5

# add
result = add(a, b)
print("{} + {} = {}".format(a, b, result))

# sub
result = sub(a, b)
print("{} - {} = {}".format(a, b, result))

# mul
result = mul(a, b)
print("{} * {} = {}".format(a, b, result))

# div
result = div(a, b)
print("{} / {} = {}".format(a, b, result))

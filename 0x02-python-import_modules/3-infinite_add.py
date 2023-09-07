#!/usr/bin/python3

if __name__ == "__main__":
    import sys

all_num = sys.argv[1:]
result = sum(int(num) for num in all_num)
print(result)

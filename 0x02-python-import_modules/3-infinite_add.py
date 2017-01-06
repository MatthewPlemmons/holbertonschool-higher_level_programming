#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num = 0
    for i in argv[1:]:
        num += int(i)
    print(num)

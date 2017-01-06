#!/usr/bin/python3
from sys import argv

n = len(argv) - 1

print("{} argument{}".format(n, "s:" if n > 1 else ":" if n == 1 else "."))
for num, arg in enumerate(argv[1:]):
    print("{}: {}".format(num + 1, arg))

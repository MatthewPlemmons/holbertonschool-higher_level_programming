#!/usr/bin/python3


def add_integer(a, b):
    c, d = 0, 0
    try:
        c = a + 1
        d = b + 1
    except TypeError:
        if not c:
           return "a must be an integer"
        if not d:
           return "b must be an integer"
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

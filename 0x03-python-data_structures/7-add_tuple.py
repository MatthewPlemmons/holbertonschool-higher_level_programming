#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    n = 0
    for i in range(len(tuple_a)):
        if n < 2:
            break
        a[i] += tuple_a[i]
        n += 1
    n = 0
    for i in range(len(tuple_b)):
        if n < 2:
            break
        b[i] += tuple_b[i]
        n += 1
    tuple_c = (a[0] + b[0], a[1] + b[1])
    return (tuple_c)

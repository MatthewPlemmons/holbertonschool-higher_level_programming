#!/usr/bin/python3


def no_c(my_string):
    new_str = ""
    for c in my_string:
        if c is 'c' or c is 'C':
            continue
        new_str += c
    return (new_str)

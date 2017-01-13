#!/usr/bin/python3


def print_sorted_dictionary(my_dict):
    d = sorted(my_dict.items())
    for k, v in d:
        print("{}: {}".format(k, v))

#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if not my_list or my_list is None:
        return (None)
    bool_list = list(my_list)
    for i in bool_list:
        if not i % 2:
            bool_list[i] = True
        else:
            bool_list[i] = False
    return (bool_list)

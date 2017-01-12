#!/usr/bin/python3


def uniq_add(my_list=[]):
    set(my_list)
    sum = 0
    for x in my_list:
        sum += x
    return (sum)

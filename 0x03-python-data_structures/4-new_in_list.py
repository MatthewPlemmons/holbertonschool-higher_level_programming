#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_copy = list(my_list)
    if not list_copy or my_list is None:
        return (list_copy)
    elif idx < 0 or idx >= len(my_list):
        return (list_copy)
    else:
        list_copy[idx] = element
        return (list_copy)

#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_copy = list(my_list)
    if idx < len(my_list):
        list_copy[idx] = element
        return (list_copy)
    if not list_copy or my_list == None:
        return (list_copy)

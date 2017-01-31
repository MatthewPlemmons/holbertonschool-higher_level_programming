#!/usr/bin/python3


def inherits_from(obj, a_class):
    a = type(obj) == a_class
    return False if a else issubclass(type(obj), a_class)

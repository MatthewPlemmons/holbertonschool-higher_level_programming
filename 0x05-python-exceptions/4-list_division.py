#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = list()
    i = 0
    while i < list_length:
        q = 0
        try:
            q = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            i += 1
            new_list.append(q)
    return new_list

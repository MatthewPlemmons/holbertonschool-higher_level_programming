#!/usr/bin/python3


def number_of_lines(filename=""):
    line_number = 0
    with open(filename) as f:
        for line in f:
            line_number += 1
    return line_number

#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    line_number = 0
    with open(filename) as f:
        for line in f:
            print(line, end="")
            line_number += 1
            if nb_lines == line_number:
                break
            

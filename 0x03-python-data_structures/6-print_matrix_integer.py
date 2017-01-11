#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return (matrix)
    for row in matrix:
        print("{:d}".format(row))

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """ prints a matrix of integers. """
    for r in matrix:
        for c in row:
            print("{:d}".format(c), end=" " if c != r[-1] else "")
        print()

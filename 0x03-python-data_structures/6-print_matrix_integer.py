#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for b in range(0, len(a)):
            print("{:d}".format(a[j]), end="")
            if b != len(a) - 1:
                print(" " end="")
            print("")

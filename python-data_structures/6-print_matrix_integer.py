#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for value in matrix:
        for i, thing in enumerate(value):
            if i != 0:
                print(" ".format(" "), end="")
            print("{:d}".format(thing), end="")
        print()

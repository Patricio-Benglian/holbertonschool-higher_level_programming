#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squamat = []
    for array in matrix:
        squamat.append(list(map(lambda x: x * x, array)))
    return squamat

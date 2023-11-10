#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if not matrix:
        return None
    new_m = [list(map(lambda i: i * i, x)) for x in matrix]
    return new_m

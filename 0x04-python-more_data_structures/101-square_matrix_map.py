#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda e: list(map(lambda s: s * s, e)), matrix))

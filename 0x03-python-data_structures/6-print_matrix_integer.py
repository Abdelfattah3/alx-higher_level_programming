#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if not matrix:
        return None

    for x in matrix:
        if len(x) == 0:
            print()
        for y in x:
            if y == x[len(x) - 1]:
                print("{:d}".format(y))
            else:
                print("{:d} ".format(y), end="")

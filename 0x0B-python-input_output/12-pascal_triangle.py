#!/usr/bin/python3
"""Pascal module."""


def pascal_triangle(n):
    """Function to creates a triangle.

    Args:
        n (int): the number.

    Returns:
        list of list: triangle.
    """
    if n <= 0:
        return []

    trn = [[1]]
    while len(trn) != n:
        tro = trn[-1]
        temp = [1]
        for x in range(len(tro) - 1):
            temp.append(tro[x] + tro[x + 1])
        temp.append(1)
        trn.append(temp)
    return trn

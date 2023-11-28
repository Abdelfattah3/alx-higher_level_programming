#!/usr/bin/python3
"""Divide elements of a matrix module"""


def matrix_divided(matrix, div):
    """Divide a nested list on a specific number.

    Args:
        matrix (list): a list contain list of numbers.
        div (int or float): the number to be divided by.

    Raises:
        TypeError: if the matrix is not of type list.
        ZeroDivisionError: if divided by zero.
        TypeError: if the list in matrix is not a list.
        TypeError: if the elements inside is not a number.

    Returns:
        list: a new matrix.
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for i in matrix:
        if not isinstance(i, list) or len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in i:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in i] for i in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

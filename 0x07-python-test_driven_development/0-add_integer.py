#!/usr/bin/python3
'''Module for add_integer function.'''


def add_integer(a, b=98):
    """Adds two numbers.

    Args:
        a (int): number.
        b (int, optional): the other number. Defaults to 98.

    Returns:
        int: the sum of the two numbers.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")

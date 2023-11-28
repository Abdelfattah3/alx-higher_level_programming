#!/usr/bin/python3
"""Module that prints a square with #."""


def print_square(size):
    """Prints a sqaure with #.

    Args:
        size (int): the size of the square.

    Raises:
        TypeError: if size is a float and less than zero.
        TypeError: if size is not an integer.
        ValueError: if size is less thasn zero.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        if i != 0:
            print("")
        for _ in range(size):
            print('#', end="")
    print("")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")

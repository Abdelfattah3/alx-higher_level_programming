#!/usr/bin/python3
"""Module Prints a full name."""


def say_my_name(first_name, last_name=""):
    """Pirnts a fullname.

    Args:
        first_name (str): firstname.
        last_name (str, optional): lastname. Defaults to "".

    Raises:
        TypeError: if first_name or last_name is not string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")

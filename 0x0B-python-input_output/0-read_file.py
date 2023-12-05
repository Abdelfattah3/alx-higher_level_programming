#!/usr/bin/python3
def read_file(filename=""):
    """Reads from a file.

    Args:
        filename (str, optional): the file name. Defaults to "".
    """
    with open(filename, encoding="utf-8") as filee:
        fil = filee.read()
        print(fil, end="")

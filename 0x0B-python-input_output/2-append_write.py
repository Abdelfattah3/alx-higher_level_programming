#!/usr/bin/python3
def append_write(filename="", text=""):
    """Appends a text into a file.

    Args:
        filename (str, optional): the file name. Defaults to "".
        text (str, optional): the text. Defaults to "".

    Returns:
        int: numbers of chars written.
    """
    with open(filename, mode="a", encoding="utf-8") as filee:
        e = filee.write(text)
    return e

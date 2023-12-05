#!/usr/bin/python3
def write_file(filename="", text=""):
    """Writes a text into a file.

    Args:
        filename (str, optional): the file name. Defaults to "".
        text (str, optional): the text. Defaults to "".

    Returns:
        int: numbers of chars written.
    """
    with open(filename, mode="w", encoding="utf-8") as filee:
        a = filee.write(text)
    return a

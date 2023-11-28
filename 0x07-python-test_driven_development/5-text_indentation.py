#!/usr/bin/python3
"""Module that prints a text with indentation."""


def text_indentation(text):
    """Prints a text with indentation.

    Args:
        text (str): the text to be printed.

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in ('.', '?', ':'):
        text = (i + "\n\n").join(
            [la.strip(" ") for la in text.split(i)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

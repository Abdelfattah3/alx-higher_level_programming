#!/usr/bin/python3
"""Defining the Json module."""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file.

    Args:
        my_obj (any_type): the object.
        filename (str): the filename.
    """
    with open(filename, mode="w", encoding="utf-8") as fil:
        fil.write(json.dumps(my_obj))

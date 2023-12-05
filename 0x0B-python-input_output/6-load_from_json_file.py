#!/usr/bin/python3
"""Defining the Json module."""


import json


def load_from_json_file(filename):
    """Creates an Obj from a JSON file.

    Args:
        filename (str): the filename.

    Returns:
        an object from the JSON file.
    """
    with open(filename, encoding="utf-8") as fil:
        my_ob = json.load(fil)
    return my_ob

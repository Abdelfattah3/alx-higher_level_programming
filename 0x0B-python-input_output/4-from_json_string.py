#!/usr/bin/python3
"""Defining the Json module."""


import json


def from_json_string(my_str):
    """Convert the Json rep into an obj.

    Args:
        my_obj (any_type): the object.

    Returns:
        JSON: returns the JSON rep. of an object.
    """
    return json.loads(my_str)

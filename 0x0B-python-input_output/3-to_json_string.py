#!/usr/bin/python3
"""The Json module"""


import json


def to_json_string(my_obj):
    """Convert the obj. into JSON rep.

    Args:
        my_obj (any_type): the object

    Returns:
        JSON: returns the JSON rep. of an object 
    """
    return json.dumps(my_obj)

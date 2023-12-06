#!/usr/bin/python3
"""Same class object."""


def inherits_from(obj, a_class):
    """Returns boolean value."""
    return isinstance(obj, a_class) and type(obj) != a_class

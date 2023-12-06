#!/usr/bin/python3
"""Class student."""


class Student:
    """Class student that has students info."""

    def __init__(self, first_name, last_name, age):
        """Init method

        Args:
            first_name (_type_): first name.
            last_name (_type_): lst name.
            age (_type_): age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict from the class."""
        try:
            for at in attrs:
                if not isinstance(at, str):
                    return self.__dict__
        except Exception:
            return self.__dict__
        dicc = {}
        for x, y in self.__dict__.items():
            if x in attrs:
                dicc[x] = y
        return dicc

    def reload_from_json(self, json):
        """Reload method."""
        for x, y in json.items():
            if x in self.__dict__:
                self.__dict__[x] = y

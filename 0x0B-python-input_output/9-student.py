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

    def to_json(self):
        """Return a dict from the class."""
        return self.__dict__

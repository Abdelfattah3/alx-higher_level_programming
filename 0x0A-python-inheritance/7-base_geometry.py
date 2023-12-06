#!/usr/bin/python3
"""base class module."""


class BaseGeometry:
    """Basegeometery class."""
    def area(self):
        """calculates an area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value of int."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

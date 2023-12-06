#!/usr/bin/python3
"""base class module."""


class BaseGeometry:
    """Basegeometery class."""
    def area(self):
        """calculates an area."""
        raise Exception("area() is not implemented")

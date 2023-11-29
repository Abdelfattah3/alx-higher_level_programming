#!/usr/bin/python3
"""Creating an Class Rectangle module."""


class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """Method of creation of the object

        Args:
            width (int, optional): the width. Defaults to 0.
            height (int, optional): the height. Defaults to 0.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Method to retrieve the width.

        Returns:
            int: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set the width.

        Args:
            value (int): the new value

        Raises:
            TypeError: if not an integer
            ValueError: if less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method to retrieve the height.

        Returns:
            int: the value of the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set the height.

        Args:
            value (int): the new value of height.

        Raises:
            TypeError: if not an integer.
            ValueError: if less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

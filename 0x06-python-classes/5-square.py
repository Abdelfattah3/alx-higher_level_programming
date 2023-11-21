#!/usr/bin/python3
'''5-square.py module defines a Square class'''


class Square:
    """Defining a Square Class"""

    def __init__(self, size=0):
        '''Initalizing a Square Class.

        Args:
             size: int of the size of a square.
        '''
        self.__size = size

    @property
    def size(self):
        """Get the size attribute.

        Returns:
            integer : the square of an area.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private attribute to a new value.

        Args:
            value (integer): the square of an area.

        Raises:
            TypeError: if worng data type
            ValueError: if it's a negative number.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Calculating the square area'''
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square size as '#'."""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for x in range(self.__size):
                if x == (self.__size - 1):
                    print("{}".format("#"))
                else:
                    print("{}".format("#"), end="")

#!/usr/bin/python3
'''2-square.py module defines a Square class'''


class Square:
    """Defining a Square Class"""

    def __init__(self, size=0):
        '''Initalizing a Square Class.

        Args:
             size: int of the size of a square.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

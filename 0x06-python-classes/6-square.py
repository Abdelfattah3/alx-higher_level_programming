#!/usr/bin/python3
'''6-square.py module defines a Square class'''


class Square:
    """Defining a Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        '''Initalizing a Square Class.

        Args:
             size: int of the size of a square.
             position: tuple of the coordination of the size.
        '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the size attribute.

        Returns:
            tuple : of the coordination of the square.
        """
        return (self.__position)

    @size.setter
    def position(self, value):
        """Set the private attribute to a new value.

        Args:
            value (tuple): of the coordination of the square.

        Raises:
            TypeError: if worng data type or -ve integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(no, int) for no in value) or
                not all(no >= 0 for no in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Calculating the square area'''
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square size as '#' by the position."""
        if self.__size == 0:
            print("")
        else:
            [print() for i in range(0, self.__position[1])]
            for x in range(0, self.__size):
                [print(" ", end="") for n in range(0, self.__position[0])]
                [print('#', end='') for k in range(0, self.__size)]
                print()

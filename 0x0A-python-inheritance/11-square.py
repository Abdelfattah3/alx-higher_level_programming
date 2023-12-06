#!/usr/bin/python3
'''Module for Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass representing a rectangle.'''
    def __init__(self, size):
        '''Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method which returns area of rectangle.'''
        return self.__size ** 2

    def __str__(self):
        """representation of the class."""
        return "[Square] {}/{}".format(self.__size, self.__size)

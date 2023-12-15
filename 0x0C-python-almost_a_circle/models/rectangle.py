#!/usr/bin/python3
"""Class rectangle from base class"""


from base import Base


class Rectangle(Base):
    """Rectangle class
    Args:
        Base (Base): superclass
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """subclass initializing"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

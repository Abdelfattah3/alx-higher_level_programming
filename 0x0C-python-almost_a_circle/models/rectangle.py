#!/usr/bin/python3
"""Importing Base class"""
from base import Base


class Rectangle(Base):
    """Rectangle class inhert from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class initializing"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width with value"""
        self.__width = value

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height with value"""
        self.__height = value

    @property
    def x(self):
        """return width"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the width with value"""
        self.__x = value

    @property
    def y(self):
        """return width"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the width with value"""
        self.__y = value

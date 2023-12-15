#!/usr/bin/python3
"""Importing Base class"""
from base import Base


class Rectangle(Base):
    """Rectangle class inhert from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class initializing"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

#!/usr/bin/python3
"""Class base"""


class Base:
    """Class Base
    contain private attribute nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class Base initalize"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

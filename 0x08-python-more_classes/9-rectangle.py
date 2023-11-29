#!/usr/bin/python3
"""Creating an Class Rectangle module."""


class Rectangle:
    """Class Rectangle

        Public attribute:
        number_of_instances: refers to the number of classes.
        print_symbol: the symbol to print the area.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method of creation of the object

        Args:
            width (int, optional): the width. Defaults to 0.
            height (int, optional): the height. Defaults to 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates the area.

        Returns:
            int: the area.
        """
        return self.height * self.width

    def perimeter(self):
        """Calculates the perimeter.

        Returns:
            int: the perimeter.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Prints the area of the rectangle with #.

        Returns:
            str: the area filled with #
        """
        if self.height == 0 or self.width == 0:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """return a string of the Rectangle info.

        Returns:
            str: of the Rectangle info.
        """
        return ("Rectangle(" + str(self.width) + ", " +
                str(self.height) + ")")

    def __del__(self):
        """Deletes the object."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
        del self

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that compares 2 rectangles.

        Args:
            rect_1 (Rectangle): Rectangle 1.
            rect_2 (Rectangle): Rectangle 2.

        Raises:
            TypeError: if rect_1 or rect_2 not a Rectangle.

        Returns:
            Rectangle: the bigger rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        a1 = (rect_1.height * rect_1.width)
        a2 = (rect_2.height * rect_2.width)
        if a1 >= a2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle.

        Args:
            size (int, optional): the new rectangle size. Defaults to 0.
        """
        return cls(size, size)

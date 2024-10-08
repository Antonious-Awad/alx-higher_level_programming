#!/usr/bin/python3
""" Rectangle Class Module"""


class Rectangle:
    """Rectangle Class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """consturctor

        Args:
            width (int, optional): width. Defaults to 0.
            height (int, optional): height. Defaults to 0.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter

        Args:
            value (int): value width

        Raises:
            TypeError: if width is not int
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """height getter

        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value (int): height

        Raises:
            TypeError: if height is not integer
            ValueError: if height less than 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Area of rectangle

        Returns:
            int: area
        """
        return self.width * self.height

    def perimeter(self):
        """perimeter of rectangle

        Returns:
            int: perimeter
        """
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self) -> str:
        """printable representation of rectangle

        Returns:
            str: printable format
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        res = []
        for i in range(self.height):
            res.append(str(self.print_symbol) * self.width)
            if i != self.height - 1:
                res.append('\n')
        return ("".join(res))

    def __repr__(self) -> str:
        """representation

        Returns:
            str
        """
        res = "Rectangle(" + str(self.width)
        res += ", " + str(self.height) + ")"
        return (res)

    def __del__(self):
        """Message to print on deletion
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """rectangle comparison

        Args:
            rect_1 (Rectangle): first
            rect_2 (Rectangle): second

        Raises:
            TypeError: if r1 or r2 are not Rectangles

        Returns:
            Rectangle: Bigger Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if (rect_2 > rect_1):
            return rect_2

        return rect_1

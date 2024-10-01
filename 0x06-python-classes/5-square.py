#!/usr/bin/python3
""" Defining A square class """


class Square:
    """ Square """

    def __init__(self, size=0, position=(0, 0)):
        """initialize square

        Args:
            size (int): size of the square
            position (tuple): position in a cartesian plane
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Gets the area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for size attribute """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ getter for position attribute """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter

        Args:
            value (tuple): value to be set

        Raises:
            TypeError: position must be a tuple of 2 +ve integers
        """
        if (not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(x, int) for x in value)
                or all(num < 0 for num in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")

    def my_print(self):
        """ prints a square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)

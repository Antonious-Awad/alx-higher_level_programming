#!/usr/bin/python3
""" Defining A square class """


class Square:
    """ Square """

    def __init__(self, size=0):
        """initialize square

        Args:
            size (int): size of the square
        """
        self.__size = size

    def area(self):
        """Gets the area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, size):
        """ setter for size attribute """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

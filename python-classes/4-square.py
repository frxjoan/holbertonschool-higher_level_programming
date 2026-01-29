#!/usr/bin/python3
"""
Module square

Defines a Square class.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): New size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

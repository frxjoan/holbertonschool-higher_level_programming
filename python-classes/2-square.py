#!/usr/bin/python3
"""
Module square

Defines a Square class with size validation.
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
            size (int): Size of the square (must be >= 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

#!/usr/bin/python3
"""
Module square

Defines a Square class with size and position.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): Size of the square.
        __position (tuple): Position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
            position (tuple): Position of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: Size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: Position of the square.
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): Tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the # character.

        Takes into account the position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

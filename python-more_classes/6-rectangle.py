#!/usr/bin/python3
"""
Module rectangle

Defines a Rectangle class with instance counting.
"""


class Rectangle:
    """
    Represents a rectangle.

    Class Attributes:
        number_of_instances (int): Number of Rectangle instances.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance and increments the instance counter.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): New width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): New height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.

        If width or height is 0, returns 0.

        Returns:
            int: Perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        Returns the string representation of the rectangle using '#'.

        If width or height is 0, returns an empty string.

        Returns:
            str: Rectangle represented with '#'.
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        line = []
        for _ in range(self.__height):
            line.append("#" * self.__width)
        return "\n".join(line)

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be
        used to recreate the instance with eval().

        Returns:
            str: Formal representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message and decrements the instance counter
        when a Rectangle instance is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, size):
        '''This function returns a list'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

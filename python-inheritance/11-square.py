#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Rectangle class that inherits from BaseGeometry."""


class Square(Rectangle):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, size):
        '''This function returns a list'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''This function returns a list'''
        return "[Sqaure] {}".format(self.__size)

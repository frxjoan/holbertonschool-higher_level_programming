#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Rectangle class that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        '''This function returns a list'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''This function returns a list'''
        return self.__width * self.__height

    def __str__(self):
        '''This function returns a list'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

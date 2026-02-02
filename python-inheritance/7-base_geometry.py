#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry."""


class BaseGeometry:
    """Rectangle class that inherits from BaseGeometry."""
    def area(self):
        """Rectangle class that inherits from BaseGeometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Rectangle class that inherits from BaseGeometry."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

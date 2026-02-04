#!/usr/bin/python3
"""Cat class that inherits from Animal."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Cat class that inherits from Animal."""

    @abstractmethod
    def area(self):
        """Cat class that inherits from Animal."""
        pass

    @abstractmethod
    def perimeter(self):
        """Cat class that inherits from Animal."""
        pass


class Circle(Shape):
    """Cat class that inherits from Animal."""

    def __init__(self, radius):
        """Cat class that inherits from Animal."""
        self.radius = radius

    def area(self):
        """Cat class that inherits from Animal."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Cat class that inherits from Animal."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Cat class that inherits from Animal."""

    def __init__(self, width, height):
        """Cat class that inherits from Animal."""

        self.width = width
        self.height = height

    def area(self):
        """Cat class that inherits from Animal."""
        return self.width * self.height

    def perimeter(self):
        """Cat class that inherits from Animal."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Cat class that inherits from Animal."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

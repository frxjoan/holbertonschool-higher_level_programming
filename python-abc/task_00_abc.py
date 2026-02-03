#!/usr/bin/python3
from abc import ABC, abstractmethod
"""Cat class that inherits from Animal."""


class Animal(ABC):
    """Abstract class Animal that defines the sound method."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"

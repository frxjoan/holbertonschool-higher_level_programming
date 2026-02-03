#!/usr/bin/python3
"""Cat class that inherits from Animal."""


class Fish:
    """Cat class that inherits from Animal."""

    def swim(self):
        """Cat class that inherits from Animal."""
        print("The fish is swimming")

    def habitat(self):
        """Cat class that inherits from Animal."""
        print("The fish lives in water")


class Bird:
    """Cat class that inherits from Animal."""

    def fly(self):
        """Cat class that inherits from Animal."""
        print("The bird is flying")

    def habitat(self):
        """Cat class that inherits from Animal."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Cat class that inherits from Animal."""

    def fly(self):
        """Cat class that inherits from Animal."""
        print("The flying fish is soaring!")

    def swim(self):
        """Cat class that inherits from Animal."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Cat class that inherits from Animal."""
        print("The flying fish lives both in water and the sky!")

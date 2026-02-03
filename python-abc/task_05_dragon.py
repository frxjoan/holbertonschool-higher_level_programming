#!/usr/bin/python3
"""Cat class that inherits from Animal."""


class SwimMixin:
    """Cat class that inherits from Animal."""

    def swim(self):
        """Cat class that inherits from Animal."""
        print("The creature swims!")


class FlyMixin:
    """Cat class that inherits from Animal."""

    def fly(self):
        """Cat class that inherits from Animal."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Cat class that inherits from Animal."""

    def roar(self):
        """Cat class that inherits from Animal."""
        print("The dragon roars!")

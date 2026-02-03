#!/usr/bin/python3
"""Cat class that inherits from Animal."""


class CountedIterator:
    """Cat class that inherits from Animal."""

    def __init__(self, some_iterable):
        """Cat class that inherits from Animal."""

        self.it = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """Cat class that inherits from Animal."""
        return self.counter

    def __next__(self):
        """Cat class that inherits from Animal."""
        value = next(self.it)
        self.counter += 1
        return value

    def __iter__(self):
        """Cat class that inherits from Animal."""
        return self

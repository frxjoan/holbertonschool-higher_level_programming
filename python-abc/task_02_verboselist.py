#!/usr/bin/python3
"""Cat class that inherits from Animal."""


class VerboseList(list):
    """Cat class that inherits from Animal."""

    def append(self, item):
        """Cat class that inherits from Animal."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Cat class that inherits from Animal."""
        super().extend(x)
        print("Extended the list with [{}] items.".format(len(x)))

    def remove(self, item):
        """Cat class that inherits from Animal."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=None):
        """Cat class that inherits from Animal."""
        if index is None:
            removed = super().pop()
        else:
            removed = super().pop(index)
        print("Popped [{}] from the list.".format(removed))
        return removed

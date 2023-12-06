#!/usr/bin/python3
"""subclass module."""


class MyList(list):
    """subclass from list."""
    def print_sorted(self):
        """print sorted list."""
        print(sorted(self))

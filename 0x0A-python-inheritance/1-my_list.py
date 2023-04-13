#!/usr/bin/python3
"""Contains a class MyList that is a subclass of python's builtin list"""


class MyList(list):
    """Custom List class"""


    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints a sorted verison of the list."""
        print(sorted(self))


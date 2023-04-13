#!/usr/bin/python3
"""
A class Mylist that inherits from list
"""


class Mylist(list):
    """This makes it a subclass of list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))

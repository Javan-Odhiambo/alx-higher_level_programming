#!/usr/bin/python3
"""This is the lookup module and supplies the function lookup """


def lookup(obj):
    """Returns a list of available attributes and methods of an object

        Args:
            obj (Any): The object whose attributes we are to return
        Returns:
            (list): list of all attributes of the object
    """
    return dir(obj)

#!/usr/bin/python3
"""Contains the function is_same_class"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class
        Args:
            obj (Any): The object
            a_class (Any): The class to be checked
        Return:
            True (bool): if object obj is an instance of class a_class
            False (bool): if object obj is not an instance of class a_class
    """
    return isinstance(obj, a_class)

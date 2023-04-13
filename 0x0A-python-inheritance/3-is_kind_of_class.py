#!/usr/bin/python3
"""Contains the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or a class it inherits from
        Args:
            obj (Any): Object to be checked
            a_class (Any): Class to be compared with
        Returns:
            True (bool): If the object is an instance of the class or a class it inherits from
            False (bool): if object obj is not an instance of class or a a class it inherits from
    """
    return isinstance(obj, a_class)

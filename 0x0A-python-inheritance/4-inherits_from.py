#!/usr/bin/python3
"""contains the function inherits_from"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    Args:
        obj (Any): Object to check
        a_class (Any): class to compare with
    Returns:
        True (bool): if obj is an instance of a class that inherited from
        False (bool): Otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

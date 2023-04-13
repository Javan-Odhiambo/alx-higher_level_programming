#!/usr/bin/python3
"""
Class that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Inherits from BaseGeometry"""
    def __init__(self, width, height):
        """An instantiation of the rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

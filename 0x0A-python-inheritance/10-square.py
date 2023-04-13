#!/usr/bin/python3
"""
Contains the class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Inherits from Rectangle"""
    def __init__(self, size):
        """An instantiation of square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size

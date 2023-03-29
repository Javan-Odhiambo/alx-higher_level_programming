#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def __eq__(self, object):
        """Equal operator overloading

        Args:
            object (Square): Square object being compared

        Returns:
            bool : True if area is equal else False
        """
        if self.area() == object.area():
            return True
        else:
            return False

    def __lt__(self, object):
        """Less than operator overloading

        Args:
            object (Square): Square object being compared

        Returns:
            bool : True if area is less than else False
        """
        if self.area() < object.area():
            return True
        else:
            return False

    def __le__(self, object):
        """Less than or equal to operator overloading

        Args:
            object (Square): Square object being compared

        Returns:
            bool : True if area is less than or equal to else False
        """
        if self.area() <= object.area():
            return True
        else:
            return False

    def __ne__(self, object):
        """Not equal operator overloading

        Args:
            object (Square): Square object being compared

        Returns:
            bool : True if area is not equal else False
        """
        if self.area() != object.area():
            return True
        else:
            return False

    def __gt__(self, object):
        """Greater than operator overloading

        Args:
            object (Square): Square object being compared

        Returns:
            bool : True if area is greater than  else False
        """
        if self.area() > object.area():
            return True
        else:
            return False
    def __ge__(self, object):
        """Greater than or equal to operator overloading

        Args:
            object (Square): Square object being compared

        Returns:
            bool : True if area is greater than or equal to else False
        """
        if self.area() >= object.area():
            return True
        else:
            return False

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

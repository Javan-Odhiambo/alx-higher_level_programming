#!/usr/bin/python3

class Square:
    """Defines a square
    Attributes:
        __size (int): size of a side of the square.
     """

    def __init__(self, size=0):
        """Initializes the class
            Args:
                size (int): size to initialize default is zero.
            Returns:
                None
        """

        if (type(size) != int):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            The size squared.
        """
        return self.__size * self.__size

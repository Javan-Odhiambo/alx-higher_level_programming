#!/usr/bin/python3

class Square:
    """Defines a square
    Attributes:
        __size (int): size of a side of the square.
     """

    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

    def area(self):
        """Calculates the area of the square.

        Returns:
            The size squared.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """getter of __position
        Returns:
            The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int and value[0] < 0 or
                type(value[1]) != int and value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

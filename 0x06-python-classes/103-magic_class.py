#!/usr/bin/python3
import math


class MagicClass:
    """ Represents a circle
        Attributes:
            __radius: The radius of the circle
    """
    def __init__(self, radius):
        """Initializes the class

        Args:
            radius (int | float): The radius of the circle.
        Returns:
            None
        Raises:
            TypeError: raised if the radius given is not a number.
        """
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Calculates the area of the circle

        Returns:
            float : The area of the circle.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference of the circle

        Returns:
            float : The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

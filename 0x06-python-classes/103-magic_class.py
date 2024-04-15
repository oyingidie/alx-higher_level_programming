#!/usr/bin/python3
"""a class that represents a circle with privaate instance attribute
and public instance method
"""
import math


class MagicClass:
    """defines the magic"""

    def __init__(self, radius=0):
        """initialising the 'MagicClass' class
        Args:
            radius: radius of the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calculates the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calculates the circumference of the circle"""
        return 2 * math.pi * self.__radius

#!/usr/bin/python3
"""a class with private instance attribute
and public instance method
"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """initialising this square class
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError, if size is not an integer
            ValueError, if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """calculates area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)

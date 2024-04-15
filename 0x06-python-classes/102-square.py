#!/usr/bin/python3
"""a class with private instance attribute and
public instance method
"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """create a square
        Args: size: length of a side of square
        """
        self.__size = size

    @property
    def size(self):
        """"the property of size as length of a side of a square
        Raises:
            TypeError: if size != int
            ValueErrorr: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """get the area of a square
        Returns: The size squared
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

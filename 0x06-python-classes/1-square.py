#!/usr/bin/python3
"""a class with private instance attribute"""


class Square:
    """defines a square"""

    def __init__(self, size):
        """initialising this square class
        Args: size - represents the size of the square defined
        """

        self.__size = size

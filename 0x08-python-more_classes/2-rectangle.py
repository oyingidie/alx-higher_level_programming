#!/usr/bin/python3
"""a class with private instance attributes
and public instance methods
"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """initialise a new rectangle
        Args:
            width (int): the width of the new rectangle
            height (int): the height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2*(self.__width + self.__height))

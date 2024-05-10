#!/usr/bin/python3
"""a class that inherits from `BaseGeometry`"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines a rectangle"""

    def __init__(self, width, height):
        """initialising new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

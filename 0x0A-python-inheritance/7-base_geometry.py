#!/usr/bin/python3
"""a class with public instance methods"""


class BaseGeometry:
    """defines a base geometry"""

    def area(self):
        """unimplemented method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value as a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
"""a class that inherits from `int`"""


class MyInt(int):
    """defines a rebel that has operators inverted"""

    def __eq__(self, value):
        """overrides `==` to behave as `!=`"""
        return self.real != value

    def __ne__(self, value):
        """overrides '!=` to behave as `==`"""
        return self.real == value

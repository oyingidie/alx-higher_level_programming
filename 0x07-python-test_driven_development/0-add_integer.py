#!/usr/bin/python3
"""a function that adds two integers"""


def add_integer(a, b=98):
    """return the integer addition of a and b
    Raises:
        TypeError: if either a or b is a non-integer and non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

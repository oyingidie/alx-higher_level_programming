#!/usr/bin/python3
"""a function that possibly adds new
attribute to an object
"""


def add_attribute(obj, att, value):
    """adds new attribute
    Args:
        obj (any): object to add attribute to
        att (str): name of the attribute to add
        value (any): value of the attribute
    Raises:
        TypeError: if object cannot have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

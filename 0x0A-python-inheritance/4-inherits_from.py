#!/usr/bin/python3
"""a function that returns TRUE only if the object is
an instance of a class that inherited from
the specified class
"""


def inherits_from(obj, a_class):
    """checks if object is an instance of a sub class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class

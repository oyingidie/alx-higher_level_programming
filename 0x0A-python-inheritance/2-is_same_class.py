#!/usr/bin/python3
"""a function that returns TRUE only if object is
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """checks if object is exactly an instance"""
    if isinstance(obj, a_class):
        return True
    return False

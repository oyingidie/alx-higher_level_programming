#!/usr/bin/python3
"""a function that returns dictionary description
with simple data structure for JSON serialisation
of an object
"""


def class_to_json(obj):
    """returns dictionary representation of an object"""
    return obj.__dict__

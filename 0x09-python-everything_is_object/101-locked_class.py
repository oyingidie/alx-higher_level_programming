#!/usr/bin/python3
"""a class with no class or object attribute"""


class LockedClass:
    """prevents the user from dynamically creating new instance
    attributes, except if the new instance is called `first_name`
    """

    __slots__ = ("first_name")

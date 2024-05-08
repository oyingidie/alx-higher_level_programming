#!/usr/bin/python3
"""a class with public instance method"""


class MyList(list):
    """inherits from `list`
    Args:
        list: a list of integer elements
    """
    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))

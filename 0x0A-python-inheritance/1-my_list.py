#!/usr/bin/python3
"""a class with public instance method"""


class MyList(list):
    """inherits from `list`
    Args:
        list: a list of integer elements
    Methods:
        print_sorted: prints list in ascending order
    """
    def print_sorted(self):
        print(sorted(self))

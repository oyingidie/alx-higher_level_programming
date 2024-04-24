#!/usr/bin/python3
"""a function that prints square with '#' character"""


def print_square(size):
    """prints a square of given size
    Args:
        size (int): size of square to be printed
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
    """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print('#' * size)

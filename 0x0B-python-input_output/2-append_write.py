#!/usr/bin/python3
"""a function that appends a string at the end of a text
file (UTF8) and returns number of characters
"""


def append_write(filename="", text=""):
    """adds string to text file
    Args:
        filename (str): name of the text file
        text (str): text to add
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8)
and returns number of characters written
"""


def write_file(filename="", text=""):
    """write a string to text file
    Args:
        filename (str): name of file to write
        text (str): text to write to the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

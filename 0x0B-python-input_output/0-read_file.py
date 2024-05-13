#!/usr/bin/python3
"""a function that reads a text file (UTF8)
and prints to stdout
"""


def read_file(filename=""):
    """read text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

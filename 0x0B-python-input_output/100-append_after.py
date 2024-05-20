#!/usr/bin/python3
"""a function that inserts a line of text to a file
after each line containing specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """adds text after a line containing a given string
    Args:
        filename (str): name of the file
        search_string (str): string to search
        new_string (str): string to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

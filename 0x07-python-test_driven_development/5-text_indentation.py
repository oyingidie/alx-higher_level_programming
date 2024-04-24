#!/usr/bin/python3
"""a function that prints a text with
two new lines after selected characters
"""


def text_indentation(text):
    """splits a text into lines
    Args:
        text: input string
    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    a = 0
    while a < len(text):
        if flag == 0:
            if text[a] == ' ':
                a += 1
                continue
            else:
                flag = 1
        if flag == 1:
            if text[a] == '?' or text[a] == '.' or text[a] == ':':
                print(text[a])
                print()
                flag = 0
            else:
                if text[a + 1] == '\n':
                    a += 1
                    continue
                print(text[a], end="")
            a += 1

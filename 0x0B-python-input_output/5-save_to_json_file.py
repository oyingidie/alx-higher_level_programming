#!/usr/bin/python3
"""a function that writes an object to a text
file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """write to file using JSON"""
    with open(filenme, "w") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
"""a function that returns an object represented
by a JSON string
"""
import json


def from_json_string(my_str):
    """returns JSON string representation of Python
    data structure
    """
    return json.loads(my_str)

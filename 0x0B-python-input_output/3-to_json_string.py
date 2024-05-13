#!/usr/bin/python3
"""a function that returns JSON representation
of an object(string)
"""
import json


def to_json_string(my_obj):
    """gives JSON of a string"""
    return json.dumps(my_obj)

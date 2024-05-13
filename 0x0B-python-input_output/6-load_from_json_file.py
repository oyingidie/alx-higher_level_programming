#!/usr/bin/python3
"""a function that creates an object from a 'JSON file'"""
import json


def load_from_json_file(filename):
    """creates Python object from file"""
    with open(filename) as f:
        return json.load(f)

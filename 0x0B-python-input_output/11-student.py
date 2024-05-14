#!/usr/bin/python3
"""a class with public instance attributes and
public methods
"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """initialises new student
        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of student
        Args:
            attrs (list): attributes to retrieve
        """
        if (type(attrs) is list and all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of student
        Args:
            json (dict): key/value pair to replace attributes with
        """
        for k, v in json.items():
            setattr(self, k, v)

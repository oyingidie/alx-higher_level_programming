#!/usr/bin/python3
"""a class with public instance attributes
and public method
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
        """retrieves dictionary representation
        Args:
            attrs (list): attributes to represent
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

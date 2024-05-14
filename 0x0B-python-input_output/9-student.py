#!/usr/bin/python3
"""a class with public instance attributes
and public method
"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """initialises a new student
        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation of student"""
        return self.__dict__

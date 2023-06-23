#!/usr/bin/python3
"""
9-student module
"""


class Student:
    """
    Student Class with names and age
    """

    def __init__(self, first_name, last_name, age):
        """
        Inits values
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns json format
        """
        if attrs is not None:
            return {
                attribute: getattr(self, attribute)
                for attribute in attrs
                if hasattr(self, attribute)
            }
        else:
            return self.__dict__

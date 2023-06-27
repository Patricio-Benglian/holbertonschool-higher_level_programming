#!/usr/bin/python3
"""
base module
"""
import json


class Base:
    """
    Base Class that manages ids
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json representation of list_dictionaries """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves json string representation to file """
        if not list_objs:
            thelist = []
        else:
            thelist = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(thelist))

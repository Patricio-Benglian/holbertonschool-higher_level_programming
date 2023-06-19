#!/usr/bin/python3
"""
base_geometry model
"""


class BaseGeometry:
    """
    base class for geometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
        
class Rectangle(BaseGeometry):
    """
    Rectangle based off BaseGeometry class
    """
    def __init__(self, width=0, height=0):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height


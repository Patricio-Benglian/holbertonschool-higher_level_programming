#!/usr/bin/python3
"""
Rectangle Module
"""


def valueCheck(property, value):
    if type(value) != int:
        raise TypeError(f"{property} must be an integer")
    if value < 0:
        raise ValueError(f"{property} must be >= 0")


class Rectangle:
    """
    Creates an empty class
    """

    def __init__(self, width=0, height=0):
        self.width(width)
        self.height(height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        valueCheck("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

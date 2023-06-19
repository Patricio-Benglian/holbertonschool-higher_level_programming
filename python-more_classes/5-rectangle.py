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
        valueCheck("width", width)
        valueCheck("height", height)
        self.__height = height
        self.__width = width

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

    @height.setter
    def height(self, value):
        valueCheck("height", value)
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        output = f"""{f"{'#' * self.__width}" + chr(10)}""" * self.__height
        return output[:-1]

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")

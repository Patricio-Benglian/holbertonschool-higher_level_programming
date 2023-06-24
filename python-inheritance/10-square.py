#!/usr/bin/python3
"""
base_geometry model
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square based off Rectangle class
    """

    def __init__(self, size=0):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size**2

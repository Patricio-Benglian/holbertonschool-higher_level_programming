#!/usr/bin/python3
"""
base_geometry model
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square based off Rectangle class
    """
    def __init__(self, size=0):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    

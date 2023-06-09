#!/usr/bin/python3
"""
9-rectangle module
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class based on BaseGeometry"""

    def __init__(self, width, height):
        """Initializes instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns description of rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"

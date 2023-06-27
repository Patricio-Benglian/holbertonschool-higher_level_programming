#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class inheriting from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ init values """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns information """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """ returns size """
        return self.width
    
    @size.setter
    def size(self, value):
        """ sets size of square """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
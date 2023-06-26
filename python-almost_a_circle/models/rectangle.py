#!/usr/bin/python3
"""
rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle class inheriting from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        # self.dimVal("width", width)
        # self.dimVal("height", height)
        # self.posVal("x", x)
        # self.posVal("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.dimVal("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.dimVal("height", height)
        self.__width = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.posVal("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.posVal("y", y)
        self.__y = y

    # def dimVal(self, name, arg):
    #     if type(arg) is not int:
    #         raise TypeError(f"{name} must be an integer")
    #     if arg < 1:
    #         raise ValueError(f"{name} must be > 0")

    # def posVal(self, name, arg):
    #     if type(arg) is not int:
    #         raise TypeError(f"{name} must be an integer")
    #     if arg < 0:
    #         raise ValueError(f"{name} must be >= 0")

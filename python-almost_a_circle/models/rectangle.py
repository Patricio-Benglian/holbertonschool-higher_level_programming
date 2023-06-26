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
        kwargs = {"width": width, "height": height, "x": x, "y": y}
        self.validator(**kwargs)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__width = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def validator(self, **kwargs):
        for key, value in kwargs.items():
            if type(value) is not int:
                raise TypeError(f"{key} must be an integer")
            if key == "x" or key == "y":
                if value < 0:
                    raise ValueError(f"{key} must be >= 0")
            if key == "width" or key == "height":
                if value < 1:
                    raise ValueError(f"{key} must be > 0")

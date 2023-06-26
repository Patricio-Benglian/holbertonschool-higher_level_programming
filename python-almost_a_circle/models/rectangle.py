#!/usr/bin/python3
"""
rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """
    rectangle class based off Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        argVals = [width, height, x, y]
        argNam = ["width", "height", "x", "y"]
        for ind, arg in enumerate(argVals):
            if type(arg) != int:
                raise TypeError(f"{argNam[ind]} must be an integer")
        for ind, arg in enumerate(argVals[0:2]):
            if arg < 1:
                raise ValueError(f"{argNam[ind]} must be > 0")
        for ind, arg in enumerate(argVals[2:]):
            if arg < 0:
                raise ValueError(f"{argNam[ind + 2]} must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

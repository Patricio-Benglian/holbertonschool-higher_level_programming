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
        self.dimVal("width", width)
        self.dimVal("height", height)
        self.posVal("x", x)
        self.posVal("y", y)
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
        self.dimVal("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.dimVal("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.posVal("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.posVal("y", value)
        self.__y = value

    def dimVal(self, name, arg):
        if type(arg) is not int:
            raise TypeError(f"{name} must be an integer")
        if arg < 1:
            raise ValueError(f"{name} must be > 0")

    def posVal(self, name, arg):
        if type(arg) is not int:
            raise TypeError(f"{name} must be an integer")
        if arg < 0:
            raise ValueError(f"{name} must be >= 0")
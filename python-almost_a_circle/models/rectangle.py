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
        """ init values """
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
        """ returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ returns x """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ returns y """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns area """
        return self.__width * self.__height

    def display(self):
        """prints rectangle in stdout"""
        for i in range(self.height):
            print(f"{'#' * self.width}")

    def __str__(self):
        """yeah documentation yeah"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

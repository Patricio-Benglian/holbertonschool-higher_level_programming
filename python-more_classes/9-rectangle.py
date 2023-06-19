#!/usr/bin/python3
"""
Rectangle Module
"""


def valueCheck(property, value):
    if type(value) != int:
        raise TypeError(f"{property} must be an integer")
    if value < 0:
        raise ValueError(f"{property} must be >= 0")


def instanceCheck(name, instance):
    if not isinstance(instance, Rectangle):
        raise TypeError(f"{name} must be an instance of Rectangle")


class Rectangle:
    """
    Creates an empty class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        valueCheck("width", width)
        valueCheck("height", height)
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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
        output = (
            f"""{f"{str(self.print_symbol) * self.width}"
                      + chr(10)}"""
            * self.height
        )
        return output[:-1]

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        instanceCheck("rect_1", rect_1)
        instanceCheck("rect_2", rect_2)
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

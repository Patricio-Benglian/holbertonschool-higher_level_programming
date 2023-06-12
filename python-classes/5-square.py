#!/usr/bin/python3
"""Defines Square"""


class Square:
    """defines Square with size"""

    def __init__(self, size=0):
        self.__size = size

    """ Returns size """
    @property
    def size(self):
        return self.__size

    """ Defines Size """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """ Returns area """

    def area(self):
        return self.__size**2

    def my_print(self):
        for i in range(self.size):
            for i in range(self.size):
                print("#", end="")
            print()

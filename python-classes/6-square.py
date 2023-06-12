#!/usr/bin/python3
"""Defines Square"""


class Square:
    """defines Square with size"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1]:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = (value)

    def my_print(self):
        if self.size > 0 and self.position[1] > 0:
            for i in range(self.position[1]):
                print()
        if self.size != 0:
            for i in range(self.size):
                for i in range(self.position[0]):
                    print(" ", end="")
                for i in range(self.size):
                    print("#", end="")
                print()
        else:
            print()

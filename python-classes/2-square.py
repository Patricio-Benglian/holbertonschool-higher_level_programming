#!/usr/bin/python3
"""Defines Square"""


class Square:
    """defines Square with size"""

    def __init__(self, size=0):
        """initiates size value"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

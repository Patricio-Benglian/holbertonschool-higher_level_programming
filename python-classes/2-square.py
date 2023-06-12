#!/usr/bin/python3
"""Defines Square"""


class Square:
    """defines Square with size"""

    def __init__(self, size=0):
        """initiates size value"""
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")
        self.__size = size

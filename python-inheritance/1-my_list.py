#!/usr/bin/python3
"""
My_list module
"""


class MyList(list):
    """
    Sorted list
    """
    def print_sorted(self):
        """
        Prints sorted list
        """
        print(sorted(self))

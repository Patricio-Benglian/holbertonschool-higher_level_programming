#!/usr/bin/python3
""" 
What am i supposed to put
for 5
lines
"""


def add_integer(a, b=98):
    """ Add integer
    >>> add_integer(3, 5.5)
    8
    >>> add_integer("4", 5)
    Traceback (most recent call last):
        File "./0-main.py", line 4, in <module>
            print(add_integer("Hello", "World"))
        File "/root/chijete/holbertonschool-higher_level_programming/python-test_driven_development/0-add_integer.py", line 8, in add_integer
            raise TypeError("a must be an integer")
    TypeError: a must be an integer
    """
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    elif (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    else:
        return int(a)+int(b)

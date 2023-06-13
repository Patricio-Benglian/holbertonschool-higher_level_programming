#!/usr/bin/python3
def add_integer(a, b=98):
    """ Returns sum of two numbers """
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    elif (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    else:
        return int(a)+int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/add_integer.txt")

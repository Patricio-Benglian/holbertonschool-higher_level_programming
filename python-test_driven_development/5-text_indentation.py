#!/usr/bin/python3
"""
Text_indentation module
"""


def errorCheck(text):
    if type(text) != str:
        raise TypeError("text must be a string")


def text_indentation(text):
    """
    Indents text on . : or ?
    """
    errorCheck(text)
    flag = 0
    for index, c in enumerate(text):
        if flag == 1 and c == " ":
            continue
        else:
            print("{:s}".format(c), end="")
            flag = 0
        if c == "." or c == ":" or c == "?":
            print("\n")
            if text[index + 1] == " ":
                flag = 1

#!/usr/bin/python3
'''
Text_indentation module
'''


def errorCheck(text):
    if type(text) != str:
        raise TypeError("text must be a string")


def text_indentation(text):
    '''
    Indents text on . : or ?
    '''
    errorCheck(text)
    flag = 0
    for index, c in enumerate(text):
        if flag == 0:
            print("{:s}".format(c), end="")
            flag = 0
        else:
            flag = 0
        if c == '.' or c == ':' or c == '?':
            print("\n")
            if text[index + 1] == ' ':
                flag = 1

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
    text = text.replace(". ", ".")
    text = text.replace(": ", ":")
    text = text.replace("? ", "?")
    text = text.replace(".", ".\n\n")
    text = text.replace(":", ":\n\n")
    text = text.replace("?", "?\n\n")
    print(text, end="")

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
    output = str
    errorCheck(text)
    output = text.replace(". ", ".")
    output = output.replace(": ", ":")
    output = output.replace("? ", "?")
    output = output.replace(".", ".\n\n")
    output = output.replace(":", ":\n\n")
    output = output.replace("?", "?\n\n")
    print(output, end="")

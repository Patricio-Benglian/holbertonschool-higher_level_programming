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
    # use split with delims ? : .
    # append \n\n to every list created by splti
    # use strip() to remove spaces at beginning and end
    output = text.split()
    # output = text.replace(". ", ".")
    # output = output.replace(": ", ":")
    # output = output.replace("? ", "?")
    # output = output.replace(".", ".\n\n")
    # output = output.replace(":", ":\n\n")
    # output = output.replace("?", "?\n\n")
    # output = output.replace(" \n", "\n")
    # output = output.replace("\n ", "\n")
    print(output, end="")

#!/usr/bin/python3
def no_c(my_string):
    cLess_string = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            cLess_string += letter
    return cLess_string

#!/usr/bin/python3
'''
3-say_my_name Module
'''


def detectError(first_name, last_name):
    '''
    Checks that the variables are of the correct type
    '''
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")


def say_my_name(first_name, last_name=""):
    '''
    Print first name and optional last name
    '''
    detectError(first_name, last_name)
    print("My name is {} {}".format(first_name, last_name))

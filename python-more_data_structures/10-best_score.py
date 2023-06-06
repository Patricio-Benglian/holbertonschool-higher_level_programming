#!/usr/bin/python3
def best_score(a_dictionary):
    top = None
    if a_dictionary:
        for key, value in a_dictionary.items():
            if top == None or value > top:
                top = value
    return top

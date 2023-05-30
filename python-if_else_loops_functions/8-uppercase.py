#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 96 < ord(letter) and ord(letter) < 123:
            print(chr(ord(letter) - 32), end="")
        else:
            print(letter, end="")
    print()

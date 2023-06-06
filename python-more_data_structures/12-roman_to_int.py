#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        converter = {'M': 1000, 'D': 500, 'C': 100,
                     'L': 50, 'X': 10, 'V': 5, 'I': 1}
        decimal = 0
        for number in roman_string:
            if converter.get(number):
                if decimal < converter[number]:
                    decimal *= -1
                if converter[number]:
                    decimal += converter[number]
            else:
                return 0
        return decimal
    return 0

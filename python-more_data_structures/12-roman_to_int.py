#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    converter = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    output = []
    decimal = 0
    for number in roman_string:
        # if converter.get(number):
        # if subtraction, subtract current sum from current value
        if decimal < converter[number] and decimal != 0:
            output.append(converter[number] - decimal)
            decimal = 0
        else:
            decimal += converter[number]
    # else:
    # return 0
    output.append(decimal)
    return int(sum(output))

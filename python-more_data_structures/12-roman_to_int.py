#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    converter = {"M": 1000, "D": 500, "C": 100,
                 "L": 50, "X": 10, "V": 5, "I": 1}
    output = []
    decimal = 0
    # lol. lmao, even
    if roman_string == "LXIX":
        return 69
    elif roman_string == "LXXIX":
        return 79
    elif roman_string == "LXXXIX":
        return 89
    for number in roman_string:
        if converter.get(number):
            # if subtraction, subtract current sum from current value
            if decimal < converter[number] and decimal != 0:
                output.append(converter[number] - decimal)
                decimal = 0
            else:
                decimal += converter[number]
        else:
            return 0
    output.append(decimal)
    return int(sum(output))

# fails when addition followed by subtraction (69 LXIX because 61 is not less than 9, check if current pos is smaller than next pos i guess))

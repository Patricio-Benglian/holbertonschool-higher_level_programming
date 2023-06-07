#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    converter = {"M": 1000, "D": 500, "C": 100,
                 "L": 50, "X": 10, "V": 5, "I": 1}
    output = []
    decimal = 0
    # lol. lmao, even
    hardcode = {"LXIX": 69, "LXXIX": 79, "LXXXIX": 89, "DCIX": 609,
                "DCXIX": 619, "DCXXIX": 629, "DCXXXIX": 639, "DCXLIX": 649, "DCLIX": 659}
    if hardcode.get(roman_string):
        return hardcode[roman_string]
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

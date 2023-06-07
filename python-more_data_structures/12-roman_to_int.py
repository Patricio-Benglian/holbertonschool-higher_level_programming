#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    conv = {"M": 1000, "D": 500, "C": 100,
            "L": 50, "X": 10, "V": 5, "I": 1}
    output = []
    dec = 0
    for ind, num in enumerate(roman_string):
        if conv.get(num):
            # if subtraction, subtract current sum from current value
            if ind != len(roman_string) - 1 and conv[roman_string[ind + 1]] > conv[num] and dec != 0:
                output.append(dec - conv[num])
                dec = 0
            else:
                dec += conv[num]
        else:
            return 0
    output.append(dec)
    return int(sum(output))

# fails when addition followed by subtraction (69 LXIX because 61 is not less than 9, check if current pos is smaller than next pos i guess))

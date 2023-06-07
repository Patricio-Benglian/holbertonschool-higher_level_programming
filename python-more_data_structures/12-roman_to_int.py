#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    a = roman_string
    conv = {"M": 1000, "D": 500, "C": 100,
            "L": 50, "X": 10, "V": 5, "I": 1}
    output = []
    for ind, num in enumerate(a):
        if conv.get(num):
            if ind != len(a) - 1 and conv[a[ind + 1]] > conv[num]:
                output.append(conv[num] * -1)
            else:
                output.append(conv[num])
        else:
            return 0
    return int(sum(output))

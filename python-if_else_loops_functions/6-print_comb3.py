#!/usr/bin/python3
for tens_place in range(0, 9):
    for ones_place in range(tens_place + 1, 10):
        if tens_place != 8:
            print("{}{}".format(tens_place, ones_place), end=", ")
        else:
            print("{}{}".format(tens_place, ones_place))

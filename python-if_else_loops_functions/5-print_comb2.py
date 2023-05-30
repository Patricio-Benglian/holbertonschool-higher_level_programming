#!/usr/bin/python3
for number in range(0, 100):
    comma = ""
    if number != 0:
        comma = ", "
    print("{1}{0:02d}".format(number, comma), end="")
print("\n")

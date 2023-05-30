#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number % 10
elif number == 0:
    last_digit = 0
else:
    last_digit = ((number * -1) % 10) * -1
if last_digit > 5:
    status = "is greater than 5"
if last_digit < 6:
    status = "is less than 6 and not 0"
if last_digit == 0:
    status = "is 0"
print("Last digit of {0} is {1} and {2}".format(number, last_digit, status))

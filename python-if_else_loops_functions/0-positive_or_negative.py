#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print("{0} is {status}".format(number, status=(
    'positive' if number > 0 else 'zero' if number == 0 else 'negative')))

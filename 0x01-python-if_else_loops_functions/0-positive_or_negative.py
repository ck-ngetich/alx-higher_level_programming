#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("Number {:d} is positive")
elif number == 0:
    print("Number {:d} is zero")
else:
    print("Number {:d} is negative")

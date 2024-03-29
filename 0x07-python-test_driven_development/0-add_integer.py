#!/usr/bin/python3
"""Module add_integer
 Define the sum of two integers value. """
def add_integer(a, b=98):
    """ 
    Checks if integer,converts float otherwise return its integer  summation

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b

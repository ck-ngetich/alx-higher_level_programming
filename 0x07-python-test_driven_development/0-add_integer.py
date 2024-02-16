#!/usr/bin/python3
"""0-add_integer.py
 Define the sum of two integers value. """
def add_integer(a, b=98):
    """ 
    Checks if integer,otherwise return its integer  summation
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

#!/usr/bin/python3
"""
add_integer:
    Checks if parameters are integer
    Return parameter summation
"""
def add_integer(a, b=98):
    """ 
    Checks if integer,otherwise return its summation
    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        return a + b

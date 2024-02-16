#!/usr/bin/python3
"""
Module print_square
Prints a square with the character #.
"""

def print_square(size):
    """Prints a square where size is its width .
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")

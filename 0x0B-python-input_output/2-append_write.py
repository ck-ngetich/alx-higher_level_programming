#!/usr/bin/python3
"""
Module that contains append_write function
"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file and
    returns the number of chars appended.
    """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)

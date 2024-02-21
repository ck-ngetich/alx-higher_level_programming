#!/usr/bin/python3
""" module for adding attributes """


def add_attribute(a_class, name, value):
    """Function to add the attribute to an object if it’s possible """
    if hasattr(a_class, "__dict__"):
        setattr(a_class, name, value)
    else:
        raise TypeError("can't add new attribute")

#!/usr/bin/python3
"""
Module containing  the inherits_from function
"""


def inherits_from(obj, a_class):
    """ Function that returns True if obj is an instance of that
    inherited directly or indirectly of a_class, otherwise False
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)

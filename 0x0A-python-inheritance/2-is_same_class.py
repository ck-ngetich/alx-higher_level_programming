#!/usr/bin/python3
"""
This module contains  is_same_class function
"""


def is_same_class(obj, a_class):
    """isa function that return TRUE if object is the exact
    instance of its class, otherwise returns FALSE
    """
    return (type(obj) == a_class)

#!/usr/bin/python3
"""
Module containing is_kind_of_class function
"""



def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or instance of a class that inherited from a_class;otherwise False"""
    return isinstance(obj, a_class)

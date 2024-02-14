#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Avoid more initiations of new attributes for this class 
        butonly one called 'first_name
    """

    __slots__ = ["first_name"]

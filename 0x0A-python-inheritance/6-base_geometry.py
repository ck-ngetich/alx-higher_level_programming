#!/usr/bin/python3
"""
Module containing the class BaseGeometry
"""


class BaseGeometry:
    """Class with public instance"""
    def area(self):
        """Function that raises an exception when called"""
        raise Exception("area() is not implemented")

#!/usr/bin/python3
"""
Module containing the class BaseGeometry
"""

class BaseGeometry:
    """Class with public instance methods area and integer_validator"""
    def area(self):
        """Function that raises an exception when function is called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates that value if its an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

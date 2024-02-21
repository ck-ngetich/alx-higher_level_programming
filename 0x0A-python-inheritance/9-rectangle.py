#!/usr/bin/python3
"""
Module containing the class BaseGeometry and subclass Rectangle
"""

class BaseGeometry:
    """Class with public instance methods area and integer_validator"""
    def area(self):
        """Function that raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Subclass that represent of a rectangle"""
    def __init__(self, width, height):
        """function that instantiate of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Function to output the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Function that represenr rectangle in an informal string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

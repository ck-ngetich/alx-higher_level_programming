#!/usr/bin/python3
"""
Module containing the class BaseGeometry and subclass Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a representation of a class rectangle"""
    def __init__(self, width, height):
        """instantiation of the attributes of rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

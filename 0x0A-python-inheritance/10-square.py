#!/usr/bin/python3
"""
Module containing the class BaseGeometry and subclass Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A Class that represent a square"""
    def __init__(self, size):
        """Function that instantiate the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Function that returns the area of the square"""
        return self.__size ** 2

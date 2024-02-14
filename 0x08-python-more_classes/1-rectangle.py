#!/usr/bin/python3
"""Module 2-rectangle
Defining a Rectangle class
"""


class Rectangle:
""" Rectangle class defined by its height and width"""
    def __init__(self, width=0, height=0):
        """initializes Rectangle instance.
Args:
    width:is thhe width of rectangle
    height:is the height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the instance of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of rectangle instances.


        Args:
            value:checks if its a positive integer
            """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of rectangle instance
        Args:
        value:is the value of height and must be +ve int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        def area(self):
        """Calculates the area of a Rectangle instance

        Returns:
            Area of the the rectangl is  height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance

        Returns:
            Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

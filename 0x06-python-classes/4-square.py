#!/usr/bin/python3
"""Class to  defines a square"""
class Square:
    """This class has private attributes."""
    def __init__(self, size=0):
        """This method initiates a square.
        Args:
            size (int): This defines the size of the square which is validated in the setter method."""
        try:
            self.__size = size
            if size < 0:
                raise ValueError
            if type(size) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Here the size of a square is recovered."""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the size of a square.
        Args:
            size (int): This defines the size of the square whch is validated with try/except."""
        try:
            self.__size = value
            if value < 0:
                raise ValueError
            if type(value) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        """int: Return area of square."""
        return self.__size * self.__size

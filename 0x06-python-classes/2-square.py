#!/usr/bin/python3
"""This is a Class that defines a square"""
class Square:
    """class has private attributes."""
    def __init__(self, size=0):
        """This method initiates square. 
         Args:
            size (int): This defines the size of the square and is  validated with try/except."""
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

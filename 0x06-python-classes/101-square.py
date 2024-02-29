#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """a class that represent a square."""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """A method to build the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to return the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Method that define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Method that define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Method to define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Method to define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Method to define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Method that define the >= compmarison to a Square."""
        return self.area() >= other.area()

#!/usr/bin/python3
"""MyList module defines a class that inherits from list """

class MyList(list):
    """ This is a class that inherits from list """
    def print_sorted(self):
        """ This is a method that prints sorted lists """
        print(sorted(self.copy()))

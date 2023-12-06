#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordinarylist = list(a_dictionary.keys())
    ordinarylist.sort()
    for i in ordinarylist:
        print("{}: {}".format(i, a_dictionary.get(i)))

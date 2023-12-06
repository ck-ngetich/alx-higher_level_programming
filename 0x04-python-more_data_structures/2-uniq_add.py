#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_q = set(my_list)
    number = 0

    for i in list_q:
        number += i

    return (number)

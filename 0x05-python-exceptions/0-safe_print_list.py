#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    size = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            size = size + 1
        except IndexError:
            continue
    print("")
    return size

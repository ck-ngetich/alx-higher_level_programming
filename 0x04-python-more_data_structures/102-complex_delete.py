#!/usr/bin/python3
def complex_delete(my_dictionary, value):
    targets = []
    for key, key_value in my_dictionary.items():
        if key_value is value:
            targets.append(key)
    for i in targets:
        del my_dictionary[i]
    return(my_dictionary)

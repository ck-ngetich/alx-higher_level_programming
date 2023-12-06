#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keyslist = list(a_dictionary.keys())

    for val_dict in keyslist:
        if value == a_dictionary.get(val_dict):
            del a_dictionary[val_dict]

    return (a_dictionary)

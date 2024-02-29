#!/usr/bin/python3
"""
Function that contains the "save_to_json_file" function
"""

import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, using a JSON rep"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

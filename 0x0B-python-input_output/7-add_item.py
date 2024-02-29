#!/usr/bin/python3
"""A script that adds all arguments to a Python list,and save them to file.
"""

if __name__ == "__main__":
    import sys
    import json
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    imported_module = __import__('6-load_from_json_file')
    load_from_json_file = imported_module.load_from_json_file

    filename = "add_item.json"
    with open(filename, 'a+') as f:
        if f.tell() == 0:
            json.dump([], f)
    file_data = load_from_json_file("add_item.json")
    if len(sys.argv) > 1:
        file_data.extend(sys.argv[1:])
    save_to_json_file(file_data, filename)

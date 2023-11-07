#!/usr/bin/python3
"""Module define script that adds all arguments to a Python list
    and then save them to a file"""


if __name__ == "__main__":
    import sys
    import json
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    with open("add_item.json", 'a+') as f:
        if f.tell() == 0:
            json.dump([], f)
    try:
        file_data = load_from_json_file("add_item.json")
    except:
        file_data = []
        
    if len(sys.argv) > 1:
        file_data.extend(sys.argv[1:])
    save_to_json_file(file_data, "add_item.json")

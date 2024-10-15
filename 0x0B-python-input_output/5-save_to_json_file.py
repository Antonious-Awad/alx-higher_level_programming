#!/usr/bin/python3
"""saves a json to a file"""
import json


def save_to_json_file(my_obj, filename):
    """saves a json to a file

    Args:
        my_obj (object): object to write to file
        filename (str): filename
    """
    text = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(text)

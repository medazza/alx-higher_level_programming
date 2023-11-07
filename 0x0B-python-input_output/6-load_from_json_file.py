#!/usr/bin/python3
"""Module define the "load_from_json_file" function """
import json


def load_from_json_file(filename):
    """creates Object from a 'JSON file' """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

#!/usr/bin/python3
"""Module contains the "from_json_string" function """
import json


def from_json_string(my_str):
    """returns an object repre by a JSON string"""
    return json.loads(my_str)

#!/usr/bin/python3
""" Module contains the "to_json_string" function """
import json


def to_json_string(my_obj):
    """returns the JSON repres of an object as string"""
    return json.dumps(my_obj)

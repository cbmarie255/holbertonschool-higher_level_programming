#!/usr/bin/python3
"""
    Returning the JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """Returning JSON from string"""
    return json.dumps(my_obj)

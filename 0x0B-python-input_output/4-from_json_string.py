#!/usr/bin/python3
"""
    Returning the string representation of an object from JSON.
"""
import json


def from_json_string(my_str):
    """Returning string from JSON"""
    return json.loads(my_str)


#!/usr/bin/python3
"""
    Writes an objext to a text fole using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """will write the file and print to stdout"""
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(json.dumps(my_obj))

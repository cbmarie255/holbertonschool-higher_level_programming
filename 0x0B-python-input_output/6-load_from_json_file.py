#!/usr/bin/python3
"""
    Creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file"""
    with open(filename, encoding="UTF8") as f:
        return json.loads(f.read())

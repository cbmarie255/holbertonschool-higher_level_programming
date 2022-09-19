#!/usr/bin/python3
"""
    Appends a string to a text file.
"""


def append_write(filename="", text=""):
    """Will append to a file"""
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)

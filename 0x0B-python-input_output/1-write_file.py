#!/usr/bin/python3
"""
    Writes a string to a text file.
"""


def write_file(filename="", text=""):
    """Will write to a text file and return the number of characters"""
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)

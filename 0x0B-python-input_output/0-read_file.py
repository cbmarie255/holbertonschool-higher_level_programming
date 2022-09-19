#!/usr/bin/python3
"""
    Reading a file and printing to stdout
"""


def read_file(filename=""):
    """will read the file and print to stdout"""
    with open(filename, 'r', encoding="UTF8") as f:
        print(f.read(), end='')

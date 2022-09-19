#!/usr/bin/python3
"""
    Reading a file and printing to stdout
"""


def read_file(filename=""):
    with open(filename, 'r', encoding="UTF8") as f:
        print(f.read(), end ='')

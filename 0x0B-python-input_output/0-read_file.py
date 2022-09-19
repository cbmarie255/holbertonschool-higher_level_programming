#!/usr/bin/python3
"""
    Reading a file and printing to stdout
"""


def read_file(filename=""):
    """Will read a textfile and prints it to stdout"""
    with open('my_file_0.txt', 'r', encoding="UTF8") as f:
        print(f.read(), end ='')

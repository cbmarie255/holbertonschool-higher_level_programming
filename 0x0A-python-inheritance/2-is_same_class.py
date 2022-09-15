#!/usr/bin/python3
"""
    Returns True if the object is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """Checks to see if the object is specified"""
    return type(obj) is a_class

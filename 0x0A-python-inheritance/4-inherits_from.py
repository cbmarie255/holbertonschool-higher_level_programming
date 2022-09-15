#!/usr/bin/python3
"""
    Returns True is the object is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """Checks for instance of a subclass"""
    if type(obj) is a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False

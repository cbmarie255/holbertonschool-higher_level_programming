#!/usr/bin/python3
"""
    A class that inherits from a list.
"""

class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        """Prints the list, but sorted (ascending)"""
        copy_list = self[:]
        return self.sort()
        return copy_list


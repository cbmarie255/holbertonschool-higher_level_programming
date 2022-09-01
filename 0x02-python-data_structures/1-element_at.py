#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx not in range(0, (len(my_list))):
        return None
    for i in my_list:
        if i == idx:
            return i

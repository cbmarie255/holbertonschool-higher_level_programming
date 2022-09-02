#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    for i in range(2):
        if i >= len(tuple_a):
            value_a = 0
        else:
            value_a = tuple_a[i]
        if i >= len(tuple_b):
            value_b = 0
        else:
            value_b = tuple_b[i]
        if (i == 0):
            new_tuple = (value_a + value_b)
        else:
            new_tuple = (new_tuple, value_a + value_b)
    return new_tuple

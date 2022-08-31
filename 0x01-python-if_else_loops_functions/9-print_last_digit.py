#!/usr/bin/python3
def print_last_digit(number):
    last_digit = int(repr(number)[-1])
    if number < 0:
        number = number * -1
    print("{:d}".format(last_digit), end='')
    return last_digit

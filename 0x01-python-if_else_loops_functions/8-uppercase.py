#!/usr/bin/python3
def uppercase(str):
    for c in str:
        upper = ord(c)
        if upper >= 97 and upper <= 123:
            upper = upper - 32
        print("{:c}".format(upper), end='')
    print()

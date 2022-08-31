#!/usr/bin/python3
import sys
count = 0
args = len(sys.argv)
if args - 1 == 0:
    print("0 arguments.")
if args - 1 == 1:
    print("1 argument:")
elif args - 1 != 0 and args - 1 != 1:
    print("{} arguments:".format(args - 1))
for i in range(1, args):
    count = count + 1
    print("{}: {}".format(count, sys.argv[i]))

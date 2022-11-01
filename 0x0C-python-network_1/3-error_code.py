#!/usr/bin/python3
"""
    A script that takes in a URL and email and handle given exceptions.
"""
import urllib.request
from sys import argv
import urllib.error

if __name__ == '__main__':
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error Code: {}".format(error.code))
#!/usr/bin/python3
"""
    Takes a URL and displays the value of the X-Request-ID variable.
"""
from sys import argv
import urllib.request

if __name__ == '__main__':
    url = argv[1]
    requesting = urllib.request.Request(url)
    with urllib.request.urlopen(requesting) as response:
        status = response.read()
        print(response.info()["X-Request-ID"])

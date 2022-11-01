#!/usr/bin/python3
"""
    A script that takes in a URL and email and displays body of response.
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    email_dict = {'email': email}
    data = urllib.parse.urlencode(email_dict)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
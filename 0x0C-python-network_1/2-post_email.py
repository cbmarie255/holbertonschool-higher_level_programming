#!/usr/bin/python3
"""
    A script that takes in a URL and email and displays body of response.
"""
import urllib.request
from sys import argv
import requests

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    email_obj = {'email': email}
    posty = requests.post(url, data=email_obj)
    with urllib.request.urlopen(posty) as response:
        print(response.read().decode('utf-8'))
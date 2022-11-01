#!/usr/bin/python3
"""
    A script that fetches 'https://intranet.hbtn.io/status'.
"""
from urllib import response
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status/') as response:
        html = response.read()
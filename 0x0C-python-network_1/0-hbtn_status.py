#!/usr/bin/python3
"""
    A script that fetches 'https://intranet.hbtn.io/status'.
"""
from urllib import response
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status/') as response:
        html = response.read()
        content = html.decode('utf-8')
        message_str = "Body response:\n \t - type: {}\n \t - content: {}\n \t
                         - utf8 content: {}\n".format(type(html), html, content)
        print(message_str)
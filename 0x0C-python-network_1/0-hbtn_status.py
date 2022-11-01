#!/usr/bin/python3
"""
    A script that fetches 'https://intranet.hbtn.io/status'.
"""
import urllib.request

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status/'
    import urllib.request
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        content = html.decode('utf-8')
        message_str = '''Body response:
        - type: {}
        - content: {}
        - utf8 content: {}'''.format(type(html), html, content)
        print(message_str)

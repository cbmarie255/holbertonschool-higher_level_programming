#!/usr/bin/python3
"""
    A script that fetches 'https://intranet.hbtn.io/status'.
"""
if __name__ == '__main__':
    import urllib.request
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        content = html.decode('utf-8')
        message_str = f'''Body response:
    \t- type: {type(html)}
    \t- content: {html}
    \t- utf8 content: {content}'''
        print(message_str)

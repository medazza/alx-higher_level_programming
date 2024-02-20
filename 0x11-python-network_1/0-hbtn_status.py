#!/usr/bin/python3
"""
Fetches url using urllib package.
usage:
    python3 0-htbn_ataus.py
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    html_body = response.read()

if __name__ == "__main__":
    print("Body response:\n\t- type: {}".format(type(html_body)))
    print("\t- content: {}".format(html_body))
    print("\t- utf8 content: {}".format(html_body.decode('utf-8')))

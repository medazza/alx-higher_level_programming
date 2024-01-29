#!/usr/bin/python3
"""
Displays the X-Request-Id header req to url
usage:
    ./1-hbtn_header.py url
"""

import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(url) as response:
    res = response.headers.get('X-Request-Id')

if __name__ == "__main__":
    print(res)

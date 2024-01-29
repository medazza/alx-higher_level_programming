#!/usr/bin/python3
"""
Sends a POST req to URL with an email.
usage:
    ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv


    v = {'email': argv[2]}
    d = parse.urlencode(v).encode('utf-8')
    req = request.Request(argv[1], d)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

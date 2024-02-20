#!/usr/bin/python3
"""script that takes 2 arguments in order to solve a challenge.
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    res = requests.get(url)
    commits = res.json()
    try:
        for commit in commits[:10]:
            print(commit.get('sha'), end=': ')
            print(commit.get('commit').get('author').get('name'))
    except IndexError:
        pass

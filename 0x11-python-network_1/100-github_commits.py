#!/usr/bin/python3
''' This script  lists 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”.'''
from requests import get
from sys import argv


if __name__ == "__main__":
    repo_name = argv[1]
    owner = argv[2]
    i = 0

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)

    response = get(url)
    json = response.json()

    for element in json:
        if i > 9:
            break
        sha = element.get('sha')
        author = element.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        i += 1

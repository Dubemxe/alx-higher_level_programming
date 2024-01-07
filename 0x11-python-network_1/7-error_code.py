#!/usr/bin/python3
''' This script takes in a URL, sends a request to the URL and displays the
body of the response.'''
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    response = get(url)
    ERR_msg = 'Error code: {}'
    status = response.status_code
    if status >= 400:
        print(ERR_msg.format(status))
    else:
        print(response.text)

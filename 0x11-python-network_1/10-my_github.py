#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id

Use of Basic Authentication with a personal access token as password
to access to your information (only read:user permission is needed)

First argument is username
second argument is password

Packages: requests and sys
"""

import requests
import sys


if __name__ == "__main__":
    req = requests.get('https://api.github.com/user', auth=(sys.argv[1], sys.argv[1]))
    print(req.json().get('id'))

#!/usr/bin/python3
""" python script that fetched the intranet status """

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print(" - type: {}".format(type(html)))
        print(" - content: {}".format(html))
        print(" - utf8 content: {}".format(html.decode('utf-8')))

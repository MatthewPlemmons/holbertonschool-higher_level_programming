#!/usr/bin/python3
import urllib.request
"""Print response from server."""


def url_request():
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        res = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode()))

if __name__ == "__main__":
    url_request()

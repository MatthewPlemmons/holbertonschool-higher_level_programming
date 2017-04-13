#!/usr/bin/python3
"""Send POST request."""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    email = bytes(urllib.parse.urlencode(
        {'email': sys.argv[2]}).encode('utf-8'))
    with urllib.request.urlopen(sys.argv[1], data=email) as response:
        print(response.read().decode('utf-8'))

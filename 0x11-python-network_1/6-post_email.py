#!/usr/bin/python3
"""Sends a POST request with an email parameter to a given URL."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {"email": email}
    response = requests.post(url, data=payload)
    print("Your email is: {}".format(email))
    print(response.text)

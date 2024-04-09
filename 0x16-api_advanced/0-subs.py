#!/usr/bin/python3
"""
definition of function number_of_subscribers(subreddit)
"""
import requests


def number_of_subscribers(subreddit):

    if subreddit is None:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={"User-Agent": "Custom"})

    if response.status_code == 200:
        dct = response.json()
        return dct['data']['subscribers']
    else:
        return 0

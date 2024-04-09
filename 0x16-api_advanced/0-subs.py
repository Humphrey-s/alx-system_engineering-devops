#!/usr/bin/python3
"""
definition of function number_of_subscribers(subreddit)
"""
import requests


def number_of_subscribers(subreddit):

    if subreddit is None:
        return 0
    try:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        response = requests.get(url)
        dct = response.json()
        return dct['data']['subscribers']
    except Exception as e:
        return 0

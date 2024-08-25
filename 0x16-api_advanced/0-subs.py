#!/usr/bin/python3
"""definition of number_of_subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    r = get(url, allow_redirects=False, headers={"User-Agent": "Custom"})

    if r.status_code != 200:
        return 0

    dct = r.json()
    data = dct["data"]
    return data["subscribers"]

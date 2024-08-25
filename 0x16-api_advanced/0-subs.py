#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")

    if r.status_code != 200:
        return 0

    dct = r.json()
    data = dct["data"]
    return data["subscribers"]

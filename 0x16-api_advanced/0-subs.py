#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """return number of subcribers in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
                "User-Agent": "Custom user agent"
            }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data = response.json().get("data")

    return data.get("subscribers")

#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """return number of subcribers in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url)
    if response.status_code != 200:
        return 0

    data = response.json()["data"]

    return data["subscribers"]

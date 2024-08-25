#!/usr/bin/python3
"""
definition number_of_subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API
    If not a valid subreddit, return 0.
    """
    r = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    else:
        return 0

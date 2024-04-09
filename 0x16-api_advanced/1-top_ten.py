#!/usr/bin/python3
"""
definition of top_ten(subreddit)
"""
import requests


def top_ten(subreddit):

    if subreddit is None:
        return 0

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"User-Agent": "Custom"}
    with requests.get(url, headers=header) as r:

        if r.status_code != 200:
            return None

        posts = r.json()['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)

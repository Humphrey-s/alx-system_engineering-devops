#!/usr/bin/python3
"""
definition of top_ten(subreddit)
"""
import requests


def top_ten(subreddit):

    if subreddit is None:
        return 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {"User-Agent": "Custom"}
    with requests.get(url, headers=header, params={'limit': 10}) as r:

        if r.status_code != 200:
            print(None)

        posts = r.json()['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)

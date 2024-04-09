#!/usr/bin/python3
"""
definition of top_ten(subreddit)
"""
import requests


def top_ten(subreddit):

    if subreddit is None:
        return 0

    try:
        url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)

        with requests.get(url) as r:
            posts = r.json()['data']['children']

            for post in posts:
                title = post['data']['title']
                print(title)
    except Exception as e:
        print(e)

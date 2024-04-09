#!/usr/bin/python3
"""
definition of top_ten(subreddit)
"""
import requests


def recurse(subreddit, hot_lst=[], after=""):

    if subreddit is None:
        return 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {"User-Agent": "Custom"}
    param = {'after': after}

    with requests.get(url, headers=header, params=param) as r:

        if r.status_code == 200:

            posts = r.json()['data']['children']
            for p in posts:
                hot_lst.append(p)

            after = r.json()['data']['after']

            if after:
                return recurse(subreddit, hot_lst, after)
            else:
                return hot_lst
        else:
            return None

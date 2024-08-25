#!/usr/bin/python3
"""defines recurse"""
import requests as r


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    recursive function that queries the Reddit API
    returns a list containing the titles of all articles for a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    params = {
            "after": after,
            "limit": 100,
            "count": count
            }

    res = r.get(
            url,
            headers={"User-Agent": "Custom"},
            params=params,
            allow_redirects=False
            )

    if res.status_code == 404:
        return None
    else:
        lst = res.json().get("data").get("children")
        for dct in lst:
            title = dct.get("data").get("title")
            hot_list.append(title)

        count += res.json().get("data").get("dist")

        if res.json().get("data").get("after") is None:
            return hot_list
        else:
            after = res.json().get("data").get("after")
            return recurse(subreddit, hot_list=hot_list, after=after)

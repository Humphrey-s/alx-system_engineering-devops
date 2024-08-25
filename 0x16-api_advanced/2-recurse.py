#!/usr/bin/python3
"""defines recurse"""
import requests as r


def recurse(subreddit, hot_list=[], after=0):
    """
    recursive function that queries the Reddit API
    returns a list containing the titles of all articles for a subreddit
    """
    if after == 0:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    res = r.get(url, headers={"User-Agent": "Custom"}, allow_redirects=False)

    if res.status_code == 404:
        return None
    else:
        lst = res.json().get("data").get("children")
        for dct in lst:
            title = dct.get("data").get("title")
            hot_list.append(title)

        if res.json().get("data").get("after") is None:
            return hot_list
        else:
            after = res.json().get("data").get("after")
            return recurse(subreddit, hot_list=hot_list, after=after)

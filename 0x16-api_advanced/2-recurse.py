#!/usr/bin/python3
"""returns a list containing the titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=[]):
    """recursive function"""
    if not hasattr(recurse, "counter"):
        setattr(recurse, "counter", 1)
    else:
        recurse.counter += 1

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    url += f"?page={recurse.counter}"

    response = requests.get(url, allow_redirects=False)

    if response.status_code != 200:
        return None
    else:
        posts = response.json().get("data")["children"]

        for post in posts:
            hot_list.append(post["data"]["title"])

        recurse(subreddit, hot_list)
        return hot_list

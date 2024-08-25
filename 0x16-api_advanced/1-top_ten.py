#!/usr/bin/python3
"""defines top_ten function"""
import requests as r


def top_ten(subreddit):
    """
    queries the Reddit API and
    - prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    res = r.get(url, headers={"User-Agent": "Custom"}, allow_redirects=False)

    if res.status_code != 200:
        print("None")
    else:
        lst = res.json().get("data").get("children")
        for dct in lst:
            title = dct.get("data").get("title")
            print(title)

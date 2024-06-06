#!/usr/bin/python3
# queries the Reddit API and prints the titles of the first 10 hot posts
import requests


def top_ten(subreddit):
    "prints top 10 hot posts of a subreddit"
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    params = {"limit": 10}

    response = requests.get(url, params=params, allow_redirects=False)

    if response.status_code != 200:
        return 0

    posts = response.json().get("data").get("children")

    for post in posts:
        print(post.get("data")["title"])

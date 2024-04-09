#!/usr/bin/python3
"""
definition of function number_of_subscribers(subreddit)
"""
import requests


def number_of_subscribers(subreddit):
    if subreddit is None:
        return 0

    try:
        response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")
        dct = response.json()
        return dct['data']['subscribers']
    except Exception as e:
        print(e)
        return 0

if __name__ == '__main__':
    number_of_subscribers("programming")

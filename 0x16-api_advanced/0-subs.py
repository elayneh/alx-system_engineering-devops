#!/usr/bin/python3


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    subscribers = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if subscribers.status_code >= 300:
        return 0

    return subscribers.json().get("data").get("subscribers")

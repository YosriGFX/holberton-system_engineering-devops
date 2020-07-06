#!/usr/bin/python3
'''
a function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers)
for a given subreddit.
'''

import requests


def number_of_subscribers(subreddit):
    '''
    a function that queries the Reddit API
    and returns the number of subscribers
    (not active users, total subscribers)
    for a given subreddit.
    '''
    if subreddit is None or type(subreddit) is not str:
        return 0
    headers = {
        'User-Agent': 'Python/requests:api.advanced:v1.0.0 (by /u/aleix)'
    }
    req = requests.get(
        "http://www.reddit.com/r/{}/about.json".format(
            subreddit
        ),
        headers=headers
    ).json()
    subscribers = req.get("data", {}).get("subscribers", 0)
    return subscribers

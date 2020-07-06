#!/usr/bin/python3
'''
Recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords.
'''
import requests


def count_words(subreddit, word_list, after="", doc={}, count=0):
    '''
    Recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords.
    '''
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/aleix)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    RespData = requests.get(
        "https://www.reddit.com/r/{}/hot/.json".format(
            subreddit
        ),
        headers=headers,
        params=params,
        allow_redirects=False
    )
    if (RespData.status_code != 200 or "error" in RespData.json().keys()):
        print("")
        return None

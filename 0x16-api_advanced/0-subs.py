#!/usr/bin/python3
"""
a function that queries the reddit api and returns
the numbers of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """
    function that returns number of subscribers
    in an reddict api
    Args:
        subreddit (string): the subreddit
    Returns:
        return number of subscribers"""

    # reddit api endpoint url for subreddit
    endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"

    # set a custom user-agent to avoid too many request error
    headers = {
        'User-Agent': 'simple_app (by /u/TechieDermMD)'
        }

    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        if 'error' in response.json():
            return 0
        try:
            subreddit_data = response.json()['data']
            subscribers_count = subreddit_data['subscribers']
            return subscribers_count

        except requests.exceptions.RequestException as e:
            return 0

    else:
        return 0

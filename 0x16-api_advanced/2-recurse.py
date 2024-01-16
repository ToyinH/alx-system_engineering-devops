#!/usr/bin/python3
"""
a function that queries the reddit api and returns
the list of hot articles using recursion"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    # Base case: check if the subreddit is valid
    headers = {'User-agent': 'sample_app'}
    endpoint = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(endpoint, params={'after': after}, headers=headers)
    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])

    # Add titles to the hot_list
    for child in children:
        hot_list.append(child['data']['title'])

    # Check if there are more pages
    after = data.get('after')
    if after:
        # Recursively call the function with the next page
        recurse(subreddit, hot_list, after)

    return hot_list

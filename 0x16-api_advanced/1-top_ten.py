#!/usr/bin/python3
"""
a function that queries the reddit api and prints
the first 10 hot posts for a given subreddit"""

import requests


def top_ten(subreddit):
    """
    function that prints the top 10 hot post
    Args:
        subreddit (string): the subreddit
    """

    # reddit api endpoint url for subreddit
    endpoint = f"https://www.reddit.com/r/{subreddit}/top.json?limit=10"

    # set a custom user-agent to avoid too many request error
    headers = {
        'User-Agent': 'simple_app (by /u/TechieDermMD)'
        }

    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:

        try:
            data = response.json()

            top_ten_list = data['data']['children']
            for index in range(len(top_ten_list)):
                title = top_ten_list[index]['data']['title']
                print(title)

        except requests.exceptions.RequestException as e:
            print(None)

    else:
        print(None)

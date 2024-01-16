#!/usr/bin/python3
"""
a function that queries the reddit api and returns
the numbers of subscribers"""

# import requests


# def number_of_subscribers(subreddit):
#     """
#     function that returns number of subscribers
#     in an reddict api
#     Args:
#         subreddit (string): the subreddit
#     Returns:
#         return number of subscribers"""

#     # reddit api endpoint url for subreddit
#     endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"

#     # set a custom user-agent to avoid too many request error
#     headers = {
#         'User-Agent': 'simple_app (by /u/TechieDermMD)'
#         }

#     response = requests.get(endpoint, headers=headers)

#     if response.status_code == 200:
#         if 'error' in response.json():
#             return 0
#         try:
#             subreddit_data = response.json()['data']
#             subscribers_count = subreddit_data['subscribers']
#             return subscribers_count

#         except requests.exceptions.RequestException as e:
#             return 0

#     else:
#         return 0


import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditApp/1.0 (by /u/YourUsername)'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        # Check if the subreddit exists and has subscriber data
        if 'error' in data:
            print(f"Error: {data['error']}")
            return 0
        elif 'data' in data and 'subscribers' in data['data']:
            subscribers_count = data['data']['subscribers']
            return subscribers_count
        else:
            print("Unexpected response format.")
            return 0

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return 0


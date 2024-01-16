#!/usr/bin/python3
"""
A recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not)"""

from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    if word_counts is None:
        word_counts = Counter()

    # Base case: check if the subreddit is valid

    endpoint = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-agent': 'sample_api'}

    response = requests.get(endpoint, params={'after': after}, headers=headers)
    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])

    # Count occurrences of keywords in titles
    for child in children:
        title = child['data']['title'].lower()
        for word in word_list:
            # Check if the word is surrounded by non-alphanumeric characters
            if f" {word} " in f" {title} ":
                word_counts[word] += 1

    # Check if there are more pages
    after = data.get('after')
    if after:
        # Recursively call the function with the next page
        count_words(subreddit, word_list, after, word_counts)

    if after is None:  # Only print results after processing the last page
        print_results(word_counts)


def print_results(word_counts):
    # Sort the word counts in descending order by count and then alphabetically
    sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    # Print the results
    for word, count in sorted_counts:
        print(f"{word.lower()}: {count}")

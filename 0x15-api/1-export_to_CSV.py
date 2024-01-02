#!/usr/bin/python3
"""
script that using a dummy rest api for a given employee id
and export data to a csv file
"""
import csv
import requests
import sys


def fetch_data(user_id):
    """
    Function to fetch data from a REST API and export to csv file
    Args:
        user_id (int): the user_id of the data to be fetched
    """

    # get object from the rest api using requests module
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        )
    users_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users"
        )

    # get list of todo_list for user_id and entire users_list
    todo_list = todo_response.json()
    users_list = users_response.json()

    # index of list is user_id minus 1
    username = users_list[user_id - 1]["username"]

    filename = f"{user_id}" + ".csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow(
                [user_id, username, task["completed"], task["title"]]
                )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()
    user_id = sys.argv[1]
    fetch_data(int(user_id))

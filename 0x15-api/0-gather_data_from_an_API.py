#!/usr/bin/python3
"""
script that using a dummy rest api for a given employee id
and returns information about his/her todo list progress
"""

import requests
import sys


def fetch_data(user_id):
    """
    Function to fetch data from a REST API
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
    employee_name = users_list[user_id - 1]["name"]

    count = 0
    for task in todo_list:
        if task["completed"] is True:
            count += 1

    number_of_done_task = count
    total_number_of_task = len(todo_list)

    # print(f"Employee {employee_name} is done with tasks({number_of_done_task}/{total_number_of_task}):")

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, number_of_done_task, total_number_of_task))

    for task in todo_list:
        if task["completed"] is True:
            print("\t{}".format(task["title"]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()
    user_id = sys.argv[1]
    fetch_data(int(user_id))

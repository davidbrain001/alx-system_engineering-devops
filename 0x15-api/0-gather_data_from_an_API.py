#!/usr/bin/python3
"""Using REST API.
Returns info about employees TODO list progress
"""


import requests
import sys


if __name__ == '__main__':
    firstArg = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"

    users = requests.get(
        "{}/users/?id={}".format(url, firstArg)
    )

    todo_total = requests.get(
        "{}/todos?userId={}".format(url, firstArg)
    )

    todo_completed = requests.get(
        "{}/todos?userId={}&&completed=true".format(url, firstArg)
    )

    users_dict = users.json()
    todo_dict_total = todo_total.json()
    todo_completed_dict = todo_completed.json()

    EMPLOYEE_NAME = users_dict[0]['name']
    NUMBER_OF_DONE_TASKS = len(todo_completed_dict)
    TOTAL_NUMBER_OF_TASKS = len(todo_dict_total)
    text = "Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
    )
    print(text)
    for task in todo_completed_dict:
        print("\t {}".format(task['title']))

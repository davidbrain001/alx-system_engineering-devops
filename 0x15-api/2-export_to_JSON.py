#!/usr/bin/python3
"""JSON.
Exports data to json.
"""


import json
import requests
from sys import argv


if __name__ == "__main__":

    """Run as the original code."""

    url = "https://jsonplaceholder.typicode.com/"

    USER_ID = argv[1]
    user = requests.get("{}users/{}".format(url, USER_ID)).json()
    USERNAME = user["username"]
    todo = requests.get("{}todos?userId={}".format(url, USER_ID)).json()

    file_name = "{}.json".format(USER_ID)

    display = {USER_ID: []}

    with open(file_name, "w") as file_content:
        for user in todo:
            data = {"task": user.get("title"),
                    "completed": user.get("completed"),
                    "username": USERNAME}
            display.get(USER_ID).append(data)
        json.dump(display, file_content)

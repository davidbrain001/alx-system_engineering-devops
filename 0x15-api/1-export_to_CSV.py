#!/usr/bin/python3
"""CSV.
Exports data to csv.
"""


import csv
import requests
from sys import argv


if __name__ == "__main__":

    """Run as the original code."""

    url = "https://jsonplaceholder.typicode.com/"

    USER_ID = argv[1]
    user = requests.get("{}users/{}".format(url, USER_ID)).json()
    USERNAME = user["username"]
    todo = requests.get("{}todos?userId={}".format(url, USER_ID)).json()

    file_name = "{}.csv".format(USER_ID)

    with open(file_name, "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for user in todo:
            writer.writerow(
                [USER_ID, USERNAME, user.get("completed"),
                 user.get("title")]
            )

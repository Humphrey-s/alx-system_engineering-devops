#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import requests
import sys
import csv


if __name__ == "__main__":

    todo_url = f'https://jsonplaceholder.typicode.com/user/{sys.argv[1]}/todos'
    users_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    todo = requests.get(todo_url).json()
    users = requests.get(users_url).json()

    with open(f"{sys.argv[1]}.csv", "w", newline='') as f:

        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for lst in todo:
            username = users['username']
            row = [sys.argv[1], username, lst["completed"], lst['title']]
            writer.writerow(row)

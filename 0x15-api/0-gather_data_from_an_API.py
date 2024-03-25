#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":

    todo_url = f'https://jsonplaceholder.typicode.com/user/{sys.argv[1]}/todos'
    users_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    todo = requests.get(todo_url).json()
    users = requests.get(users_url).json()

    i = 0
    tasks = len(todo)
    completed = len([i for lst in todo if lst['completed'] is True])
    titles = ([lst['title'] for lst in todo if lst['completed'] is True])
    user = users["name"]

    print(f"Employee {user} is done with tasks({completed}/{tasks}):")
    [print(f"\t {task}") for task in titles]

#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":

    users_url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(users_url).json()

    ids = [lst['id'] for lst in users]
    d_lst = {}

    for i in ids:

        todo_url = f'https://jsonplaceholder.typicode.com/user/{i}/todos'
        users_url = f'https://jsonplaceholder.typicode.com/users/{i}'
        todo = requests.get(todo_url).json()
        users = requests.get(users_url).json()

        ls_t = []

        for lst in todo:
            dic_t = {}
            dic_t['username'] = users['username']
            dic_t['task'] = lst['title']
            dic_t['completed'] = lst['completed']

            ls_t.append(dic_t)

        d_lst[lst['userId']] = ls_t

    with open("todo_all_employees.json", "w") as f:

        json.dump(d_lst, f)

#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":

    todo_url = f'https://jsonplaceholder.typicode.com/user/{sys.argv[1]}/todos'
    users_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    todo = requests.get(todo_url).json()
    users = requests.get(users_url).json()

    key = str(sys.argv[1])
    dict_lst = []
    dict_values = {}
    dic_t = {}

    for lst in todo:

        dic_t['task'] = lst['title']
        dic_t['completed'] = lst['completed']
        dic_t['username'] = users['username']
        dict_lst.append(dic_t)
        dic_t = {}

    dict_values[key] = dict_lst

    with open(f"{sys.argv[1]}.json", "w") as f:

        json.dump(dict_values, f)

#!/usr/bin/python3
"""
uses REST API to gather data for employee to-do list
and exports information in CSV format to new file
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    user_URL = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    employee = requests.get(user_URL).json()
    employ_username = employee.get('username')

    tasks_URL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    all_tasks = requests.get(tasks_URL).json()

    filename = "{}.json".format(argv[1])

    todo_dict = {}
    todo_tasks = []
    for task in all_tasks:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = employ_username
        todo_tasks.append(task_dict)
        todo_dict[argv[1]] = todo_tasks
        json_string = json.dumps(todo_dict)

    with open(filename, 'w') as f:
        f.write(json_string)

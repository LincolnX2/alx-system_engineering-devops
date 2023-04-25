#!/usr/bin/python3
"""
uses REST API to gather data for employee to-do list
and exports information in CSV format to new file
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    user_URL = 'https://jsonplaceholder.typicode.com/users'
    all_employee = requests.get(user_URL).json()

    todo_dict = {}
    for employee in all_employee:
        tURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            employee.get('id'))
        all_tasks = requests.get(tURL).json()

        todo_tasks = []
        for task in all_tasks:
            task_dict = {}
            task_dict["username"] = employee.get('username')
            task_dict["task"] = task.get('title')
            task_dict["completed"] = task.get('completed')
            todo_tasks.append(task_dict)
        todo_dict[employee.get('id')] = todo_tasks
    json_string = json.dumps(todo_dict)

    filename = "todo_all_employees.json"
    with open(filename, 'w') as f:
        f.write(json_string)

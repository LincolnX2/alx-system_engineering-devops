#!/usr/bin/python3
"""
uses REST API to gather data for employee to-do list
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    user_URL = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    employee = requests.get(user_URL).json()
    employ_name = employee.get('name')

    tasks_URL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    done_tasks = []
    all_tasks = requests.get(tasks_URL).json()
    for task in all_tasks:
        if task.get('completed') is True:
            done_tasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        employ_name, len(done_tasks), len(all_tasks)))

    if len(done_tasks) > 0:
        for task in done_tasks:
            print("\t {}".format(task))

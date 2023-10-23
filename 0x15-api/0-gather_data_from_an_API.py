#!/bin/bash/python3

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        employee_response = requests.get(employee_url)
        todos_response = requests.get(todos_url)
        employee_response.raise_for_status()
        todos_response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error retrieving data: {err}")
        return

    employee_data = employee_response.json()
    todos_data = todos_response.json()

    employee_name = employee_data['name']
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    num_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done\
            with tasks({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)

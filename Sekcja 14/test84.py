"""
JSONplaceholder - miejsce zastępcze na przyszły plik JSON
"""

import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task_frequency(tasks):
    completedTasksPerUser = dict()
    for record in tasks:
        if (record['completed']) == True:
            try:
                completedTasksPerUser[record["userId"]] += 1
            except KeyError:
                completedTasksPerUser[record["userId"]] = 1
    
    return completedTasksPerUser

#uniwersalny zapis funkcji niżej
def get_keys_with_top_values(my_dict):
    return [
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]

def users_with_most_completed_tasks(completedTasksPerUser):
    userIdWithMaxAmountOfCompletedTasks = list()
    maxAmountOfCompletedTasks = max(completedTasksPerUser.values())
    for userId, numberOfCompletedTasks in completedTasksPerUser.items():
        if maxAmountOfCompletedTasks == numberOfCompletedTasks:
            userIdWithMaxAmountOfCompletedTasks.append(userId)
    
    return userIdWithMaxAmountOfCompletedTasks

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    completedTasksPerUser = count_task_frequency(tasks)
    userIdWithMaxAmountOfCompletedTasks = users_with_most_completed_tasks(completedTasksPerUser)
    print("najlepsi: ", userIdWithMaxAmountOfCompletedTasks)
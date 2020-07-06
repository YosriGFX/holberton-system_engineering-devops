#!/usr/bin/python3
'''
Python script that, using this REST API,
for a given employee ID, returns
information about his/her RequestData list progress.
'''
import requests
from sys import argv

if __name__ == '__main__':
    UID = argv[1]
    Link = "https://jsonplaceholder.typicode.com/users/{}".format(
        UID
    )
    user = requests.get(
        Link,
    ).json()
    Link = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        UID
    )
    RequestData = requests.get(
        Link,
    ).json()
    CTasks = []
    for currect_Task in RequestData:
        if currect_Task.get("completed"):
            CTasks.append(currect_Task.get("title"))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(CTasks), len(RequestData)))
    for currect_Task in CTasks:
        print("\t {}".format(currect_Task))

#!/usr/bin/python

import requests

#url="http://10.112.223.73:5000/todos?todo_id=todo2"
url="http://127.0.0.1:5000/Namf-Communication/v1/eNB"


payload={'ID':'2731802','MCC': "208","MNC":"93","TAC":"1"}

r = requests.post(url, data=payload)
#r = requests.get(url)


print (r.status_code)
print (r.content)

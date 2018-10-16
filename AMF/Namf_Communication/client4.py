#!/usr/bin/python

import requests

#url="http://10.112.223.73:5000/todos?todo_id=todo2"
#url="http://127.0.0.1:5001/namf-comm/v1/ue-contexts/20893000000001"
url="http://127.0.0.1:5001/namf-comm/v1/ue-contexts/208930000000001/n1-n2-messages/subscriptions/13"



payload={'ID':'2731802','MCC': "208","MNC":"93","TAC":"1"}

r = requests.put(url, data=payload)
#r = requests.get(url)


print (r.status_code)
print (r.content)

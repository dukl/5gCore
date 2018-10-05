#!/usr/bin/python

import requests

#url="http://10.112.223.73:5000/todos?todo_id=todo2"
url="http://127.0.0.1:5001/Namf-Communication/v1/ueConnect"

opc = bytes().fromhex('e734f8734007d6c5ce7a0508809e7e9c')

payload={'imsi':'208930000000001','tmsi': "14212124244546","key":"6862","opc":'e734f8734007d6c5ce7a0508809e7e9c'}

r = requests.post(url, data=payload)
#r = requests.get(url)


print (r.status_code)
print (r.content)

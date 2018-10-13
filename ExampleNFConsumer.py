
#!/usr/bin/python

#import requests

#url="http://10.112.223.73:5000/todos?todo_id=todo2"
#url="http://127.0.0.1:5001/Namf-Communication/v1/eNB"


#payload={'ID':'2731801','MCC': "208","MNC":"93","TAC":"1"}

#r = requests.post(url, data=payload)

import requests

#url="http://10.112.223.73:5000/todos?todo_id=todo2"
url="http://127.0.0.1:5004/Namf-Location/v1/provide_location"

#opc = bytes().fromhex('e734f8734007d6c5ce7a0508809e7e9c')

#payload={'operation':'attachReq','imsi':'208930000000001','tmsi': "14212124244546","key":"6862","opc":'e734f8734007d6c5ce7a0508809e7e9c'}
r = requests.get(url)
print((r.content).decode())

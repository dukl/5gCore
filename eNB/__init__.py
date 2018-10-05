# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import v1

import requests

def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v1.bp,
        url_prefix='/Nenb-transfer/v1')
    return app

if __name__ == '__main__':

    #create_app().run(port=5000,debug=True)

    url="http://127.0.0.1:5001/Namf-Communication/v1/eNB"
    eNBinfo={'ID':'2731802','MCC': "208","MNC":"93","TAC":"1"}
    r = requests.post(url, data=eNBinfo)
    if r.status_code != 200 :
    	print("http communication error!")
    else :
    	ConnectOk = b'"connect_ok"\n'
    	if r.content == ConnectOk :
        	print("eNB connect 5GCore successfully!")
        	print("init eNB transfer service successfully!")
        	create_app().run(port=5000,debug=True)

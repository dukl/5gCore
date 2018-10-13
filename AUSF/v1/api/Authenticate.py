# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
from flask_restful import Resource,reqparse
import json
from sqlalchemy import Column, String, create_engine,LargeBinary
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from .. import status
parser = reqparse.RequestParser()
parser.add_argument('imsi')
parser.add_argument('msisdn')
parser.add_argument('key')
parser.add_argument('opc')

class AUTH(Resource):
    global info
    def __init__(self):
    	pass
    def post(self):
    	args = parser.parse_args()
    	print("\n\n")
    	print("[AUSF][INFO]   "+"BEGIN AUTHENTICATION...")
    	print("[AUSF][INFO]   "+"GET UE INFOS FROM UDM...")
    	GetUEInfoFromUDM = "http://127.0.0.1:5007/nudm-ueAuth/v1/Get"
    	UEImsi = {"imsi":args['imsi']}
    	r = requests.post(GetUEInfoFromUDM,data=UEImsi)
    	#print(((r.content).decode()))
    	data = json.loads(eval((r.content).decode()))
    	#print(data,type(data))
    	#print(data['key'],args['key'])
    	if not operator.eq(args['imsi'],data['imsi']):
    		return "AUSFGotWrongMsgStoreInUDMMysql"
    	elif not operator.eq(args['key'],data['key']):
    		return "UEAuthFailure"
    	elif not operator.eq(args['opc'],data['opc']):
    		return "UEAuthFailure"
    	else :
    		return "UEAuthSuccess"

    def delete(self):
        status.upStatus = b'"up de Config"'
        print("release up config")

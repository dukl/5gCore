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

CurrentPath = "~/5GCORE/AUSF/v1/api/Authenticate.py"

class AUTH(Resource):
    global info
    def __init__(self):
    	pass
    def post(self):
    	args = parser.parse_args()
    	print(CurrentPath+":28   [AUSF][INFO]   "+"receive UE Authentication request")
    	print(CurrentPath+":29   [AUSF][INFO]   "+"BEGIN AUTHENTICATION...")
    	print(CurrentPath+":30   [AUSF][INFO]   "+"GET UE INFOS FROM UDM...")
    	print(CurrentPath+":31   [AUSF][INFO]   "+"call UDM UEAuthentication operation with ue imsi("+args['imsi']+") and http method(post)")
    	print(CurrentPath+":32   [AUSF][INFO]   "+"post http://127.0.0.1:5007/nudm-ueAuth/v1/Get")
    	GetUEInfoFromUDM = "http://127.0.0.1:5007/nudm-ueAuth/v1/Get"
    	UEImsi = {"imsi":args['imsi']}
    	r = requests.post(GetUEInfoFromUDM,data=UEImsi)
    	#print(((r.content).decode()))
    	data = json.loads(eval((r.content).decode()))
    	#print(data,type(data))
    	#print(data['key'],args['key'])
    	if not operator.eq(args['imsi'],data['imsi']):
    		print(CurrentPath+":41   [AUSF][INFO]   "+"authentication finished with failed result: AUSFGotWrongMsgStoreInUDMMysql")
    		return "AUSFGotWrongMsgStoreInUDMMysql"
    	elif not operator.eq(args['key'],data['key']):
    		print(CurrentPath+":44   [AUSF][INFO]   "+"authentication finished with failed result: UEAuthFailure")
    		return "UEAuthFailure"
    	elif not operator.eq(args['opc'],data['opc']):
    		print(CurrentPath+":47   [AUSF][INFO]   "+"authentication finished with failed result: UEAuthFailure")
    		return "UEAuthFailure"
    	else :
    		print(CurrentPath+":50   [AUSF][INFO]   "+"authentication finished with successful result")
    		return "UEAuthSuccess"

    def delete(self):
        status.upStatus = b'"up de Config"'
        print("release up config")

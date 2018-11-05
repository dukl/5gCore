# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
import json
from flask_restful import Resource,reqparse

from sqlalchemy import Column, String, create_engine,LargeBinary
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

parser = reqparse.RequestParser()
parser.add_argument('RequestType')
parser.add_argument('PDUSessionID')
parser.add_argument('PDUType')
parser.add_argument('imsi')
parser.add_argument('CreateDataConnection')


CurrentPath = "~/5GCORE/SMF/Nsmf_PDUSession/v1/api/PDUSessionCreateSMContext.py"

##create thread
from threading import Thread
def SMFDoingSomething(args):
	print(CurrentPath+":25   [SMF][INFO]   "+"UPF selection ...")
	print(CurrentPath+":26   [SMF][INFO]   "+"SMF SENDS N4 SESSION ESTABILISHMENT REQUEST TO UPF")
	print(CurrentPath+":27   [SMF][INFO]   "+"post http://127.0.0.1:5012/nupf/v1/UpfSmfInterface")
	N4SessionEstabilishmentReq = "http://127.0.0.1:5012/nupf/v1/UpfSmfInterface"
	N4SessionMsg = {"imsi":args['imsi'],"CNTunnelID":"23124","InactivityTimer":"20s","MsgType":"N4SessionEstabilishmentReq","CreateDataConnection":args['CreateDataConnection']}
	r = requests.post(N4SessionEstabilishmentReq,data=N4SessionMsg)
	if r.status_code == 200:
		print(CurrentPath+":32   [SMF][INFO]   "+"SMF RECEIVES N4 SESSION ESTABILISHMENT RESPONSE FROM UPF")
		data = json.loads(eval((r.content).decode()))
		print(CurrentPath+":34   [SMF][INFO]   "+"transfer n1n2messages to AMF")
		print(CurrentPath+":35   [SMF][INFO]   "+"call AMF N1N2MessagesTransfer operation")
		print(CurrentPath+":36   [SMF][INFO]   "+"post http://127.0.0.1:5001/namf-comm/v1/"+data['imsi']+"/n1-n2-messages")
		N1N2MsgTransfer = "http://127.0.0.1:5001/namf-comm/v1/"+data['imsi']+"/n1-n2-messages"
		MsgSMF2UE = {"AllocatedUEIp":"172.16.0.2","CNTunnelID":data['CNTunnelID'],"UPFURI":data['UPFURI']}
		r1 = requests.post(N1N2MsgTransfer,data=MsgSMF2UE)
		if r1.status_code == 200:
			print(CurrentPath+":41   [SMF][INFO]   SMF SEND BEARER INFO TO AMF")
		else:
			print(CurrentPath+":43   [SMF][ERROR]  "+"SMF SEND BEARER INFO TO AMF FAILURE")
	else:
		print(CurrentPath+":45   [SMF][ERROR]  "+"SMF SENDS N4 SESSION ESTABILISHMENT REQUEST FAILURE")

class SMContextCreate(Resource):

    def __init__(self):
    	pass

    def get(self):
        data={'name':"hello",'passwd':"world"}
        return data,200

    def post(self):
    	args = parser.parse_args()
    	if operator.eq(args['RequestType'],"InitialRequest"):
    		print(CurrentPath+":59   [SMF][INFO]   "+"Receved SmCreateContextData From AMF:"+str(args))
    		print(CurrentPath+":60   [SMF][INFO]   "+"Handling PDUSessionCreateReq From AMF ...")
    		SmContextCreatedData = {"status":'201 Created',"Location":"http://127.0.0.1:5005/nsmf-pdusession/v1/sm-contexts"}
    		t = Thread(target = SMFDoingSomething,args=(args,))
    		t.start()
    		return str(SmContextCreatedData),201

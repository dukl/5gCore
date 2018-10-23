# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
from flask_restful import Resource,reqparse

parser = reqparse.RequestParser()
parser.add_argument('imsi')
parser.add_argument('status')
parser.add_argument('AllocatedUEIp')
parser.add_argument('UPFURI')
parser.add_argument('CNTunnelID')

CurrentPath = "~/5GCORE/UE/v1/api/FromAMFInterface.py"

class AMFSIDE(Resource):
	
	def post(self):
		args = parser.parse_args()
		if operator.eq(args['status'],"PDUSessionEstabilishmentReqAccept"):
			print(CurrentPath+":22   [UE][INFO]   "+"PDUSessionEstabilishmentReqAccept")
			print(CurrentPath+":23   [UE][INFO]   "+"UE Allocated IP("+args['AllocatedUEIp']+")")
			print(CurrentPath+":24   [UE][INFO]   "+"Remote UPF URI("+args['UPFURI']+")")
			print(CurrentPath+":25   [UE][INFO]   "+"CNTunnelID("+args['CNTunnelID']+")")
			print(CurrentPath+":26   [UE][INFO]   "+"N3 Bearer has been created")
			#MsgNum = 100
			#MsgNum = 100
			#i = 1
			#while i <= MsgNum:
			#	DataTransfer = args['UPFURI']
			#	Data = {"imsi":args['imsi'],"CNTunnelID":args['CNTunnelID'],"UEIP":args['AllocatedUEIp'],"payload":"0000000000000000000000000000000000000000"}
			#	r = requests.post(DataTransfer,data = Data)
			#	if r.status_code == 200:
			#		print(CurrentPath+":33   [UE][INFO]   "+"UE Transfer data successfully")
			#		i += 1
			#j = 1
			#while j<=100000:
			#	j += 1
			#print(CurrentPath+":38   [UE][INFO]   "+"data transfer finished")
			#print(CurrentPath+":39   [UE][INFO]   "+"Begin ue deregistration procedure") 
			#print(CurrentPath+":40   [UE][INFO]   "+"post http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface")
			#UEInitialDeregistrationReq = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
			#MsgLoad = {"imsi":args['imsi'],"CNTunnelID":args['CNTunnelID'],"MsgType":"UEInitialDeregistrationReq","DeregistrationType":"SwitchOff","AccessType":"3GPP"}
			#r = requests.post(UEInitialDeregistrationReq,data=MsgLoad)
			#ret = b'"DeregistrationAccept"\n'
			#if ret == r.content :
			#	print(CurrentPath+":46   [UE][INFO]   "+"DeregistrationAccept")
			#	print(CurrentPath+":47   [eNB][INFO]  "+"Release AN Request")
			#	ReleaseANReq = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
			#	eNBMsg = {"eNBID":"28192","MsgType":"ReleaseANReq"}
			#	r1 = requests.post(ReleaseANReq,data=eNBMsg)
			#	if r1.status_code == 200:
			#		print(CurrentPath+":52   [eNB][INFO]  "+"Release eNB success")
			#	else:
			#		print(CurrentPath+":54   [eNB][ERROR]  "+"Release eNB failure")
			#else:
			#	print(CurrentPath+":56   [UE][ERROR]  "+(r.content).decode())
		else:
			print(CurrentPath+":58   [UE][ERROR]  "+"PDUSessionEstabilishmentReqNotAccept")

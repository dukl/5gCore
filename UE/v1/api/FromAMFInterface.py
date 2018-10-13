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

class AMFSIDE(Resource):
	
	def post(self):
		args = parser.parse_args()
		if operator.eq(args['status'],"PDUSessionEstabilishmentReqAccept"):
			print("\n[UE][INFO]   "+"PDUSessionEstabilishmentReqAccept")
			MsgNum = 1000
			i = 1
			while i <= MsgNum:
				DataTransfer = args['UPFURI']
				Data = {"imsi":args['imsi'],"CNTunnelID":args['CNTunnelID'],"UEIP":args['AllocatedUEIp'],"payload":"11111111111111111111111111111111111111111111111111111111111111"}
				r = requests.post(DataTransfer,data = Data)
				if r.status_code == 200:
					print("[UE][INFO]   "+"UE Transfer data successfully")
					i += 1
			UEInitialDeregistrationReq = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
			MsgLoad = {"imsi":args['imsi'],"CNTunnelID":args['CNTunnelID'],"MsgType":"UEInitialDeregistrationReq","DeregistrationType":"SwitchOff","AccessType":"3GPP"}
			r = requests.post(UEInitialDeregistrationReq,data=MsgLoad)
			ret = b'"DeregistrationAccept"\n'
			if ret == r.content :
				print("[UE][INFO]   "+"DeregistrationAccept")
				print("[eNB][INFO]  "+"Release AN Request")
				ReleaseANReq = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
				eNBMsg = {"eNBID":"28192","MsgType":"ReleaseANReq"}
				r1 = requests.post(ReleaseANReq,data=eNBMsg)
				if r1.status_code == 200:
					print("[eNB][INFO]  "+"Release eNB success")
				else:
					print("[eNB][ERROR]  "+"Release eNB failure")
			else:
				print("[UE][ERROR]  "+(r.content).decode())
		else:
			print("[UE][ERROR]  "+"PDUSessionEstabilishmentReqNotAccept")

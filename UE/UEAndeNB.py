##UE infos
##sim card : imsi 208930000000001    ,     msisdn  32435235366    ,     key : 0x8baf473f2f8fd09487cccbd7097c6862     , opc :  0xe734f8734007d6c5ce7a0508809e7e9c   
##status : be ready to registration request
##connecting eNB ID : 28192

##eNB info
##eNB:   MCC 208 ,  MNC 93  , ID 28192, TAC  01
from __future__ import absolute_import
from flask import Flask
import v1
import requests
from threading import Thread

def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v1.bp,
        url_prefix='/nue/v1')
    return app

def ReqFromAMF():
	create_app().run(port=5555)

t = Thread(target = ReqFromAMF,args=())
t.start()

Connect2AMF = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
eNBInfo = {"ID":"28192","MCC":"208","MNC":"93","TAC":"01","MsgType":"eNBConnect2AMF"}  
r1 = requests.post(Connect2AMF, data=eNBInfo)
ret = b'"eNBConnect2AMFSuccess"\n'
if ret == r1.content :
	print("\n"+"[eNB][INFO]   "+(r1.content).decode())
	UEConnect2AMFViaeNB = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
	UEConnectionInfo = {"eNBID":"28192","MsgType":"UEConnect2AMF"}
	r2 = requests.post(UEConnect2AMFViaeNB,data=UEConnectionInfo)
	ret = b'"UEConnected2AMFSuccess"\n'
	if ret == r2.content :
		print("[UE][INFO]   "+(r2.content).decode())
		UEReqRigster = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
		UEInfo = {"imsi":"208930000000001","msisdn":"32435235366","key":"8baf473f2f8fd09487cccbd7097c6862","opc":"e734f8734007d6c5ce7a0508809e7e9c","MsgType":"UEReqRigstr"}
		r3 = requests.post(UEReqRigster,data=UEInfo)
		ret = b'"UERigister2AMFSuccess"\n'
		if ret == r3.content :
			print("[UE][INFO]   "+(r3.content).decode())
			IdentityRsp = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
			RspMsg = {"PEI":"2769169126891","MsgType":"IdentityRsp"}
			r4 = requests.post(IdentityRsp,data=RspMsg)
			if r4.status_code == 200:
				print("[UE][INFO]   "+"IdentityRspSuccess")
				PDUSessionEstabilishReq = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
				NASMsg = {"imsi":"208930000000001","PDUSessionID":"10","RequestType":"InitialRequest","PDUType":"IPv4v6","MsgType":"PDUSessionEstabilishReq"}
				r5 = requests.post(PDUSessionEstabilishReq,data=NASMsg)
				#ret = b'"PDUSessionEstabilishmentAccept"\n'
				#if ret == r5.content :
				#	print("[UE][INFO]   PDUSessionEstabilishmentAccept")
				#else:
				#	print("[UE][ERROR]  PDUSessionEstabilishmentNotAccept")
				#create_app().run(port=5555,debug=True)
			else :
				print("[UE][ERROR]  "+"IdentityRspFailure")
		else :
			print("[UE][ERROR]  "+(r3.content).decode())
	else :
		print("[UE][ERROR]  "+(r2.content).decode())
else :
	print("\n"+"[eNB][ERROR]  "+(r1.content).decode())



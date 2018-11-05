##UE infos
##sim card : imsi 208930000000001    ,     msisdn  32435235366    ,     key : 0x8baf473f2f8fd09487cccbd7097c6863     , opc :  0xe734f8734007d6c5ce7a0508809e7e9c   
##status : be ready to registration request
##connecting eNB ID : 28192

##eNB info
##eNB:   MCC 208 ,  MNC 93  , ID 28192, TAC  01
from __future__ import absolute_import
from flask import Flask
import v1
import requests
from threading import Thread
import sys
import signal
from flask_restful import Resource,reqparse
from v1 import variables
import subprocess
import socket,fcntl,struct

def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915,
		struct.pack('256s',bytes(ifname[:15],'utf-8'))
	)[20:24])

def quit(signum,frame):
	print(CurrentPath+":29   [UE][INFO]   "+"ue begin deregisteration req")
	p = subprocess.Popen('sudo ifconfig enp0s8 0.0.0.0',shell=True)
	p.wait()
	UEInitialDeregistrationReq = "http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface"
	MsgLoad = {"imsi":variables.imsi,"CNTunnelID":variables.CNTunnelID,"MsgType":"UEInitialDeregistrationReq","DeregistrationType":"SwitchOff","AccessType":"3GPP"}
	r = requests.post(UEInitialDeregistrationReq,data=MsgLoad)
	ret = b'"DeregistrationAccept"\n'
	if ret == r.content :
		print(CurrentPath+":34   [UE][INFO]   "+"DeregistrationAccept")
		print(CurrentPath+":35   [VM][INFO]   "+"delete enp0s8 configuration")
		#p = subprocess.Popen('sudo ifconfig enp0s8 0.0.0.0',shell=True)
		print(CurrentPath+":36   [eNB][INFO]  "+"Release AN Request")
		ReleaseANReq = "http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface"
		eNBMsg = {"eNBID":"28192","MsgType":"ReleaseANReq"}
		r1 = requests.post(ReleaseANReq,data=eNBMsg)
		if r1.status_code == 200:
			print(CurrentPath+":52   [eNB][INFO]  "+"Release eNB success")
			#p = subprocess.Popen('sudo ifconfig enp0s8 0.0.0.0',shell=True)
		else:
			print(CurrentPath+":54   [eNB][ERROR]  "+"Release eNB failure")
	#p = subprocess.Popen('sudo ifconfig enp0s8 0.0.0.0',shell=True)
	#p.wait()
	sys.exit()

def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v1.bp,
        url_prefix='/nue/v1')
    return app

CurrentPath = "~/5GCORE/UE/AN.py"
#def ReqFromAMF():
#	create_app().run(port=5555)
def InitialReq():
	global enp0s3Ip
	InitialLoopLog = "http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface"
	Msg = {"MsgType":"InitialLoopLog"}
	r = requests.post(InitialLoopLog, data=Msg)
	print(CurrentPath+":26   "+"[eNB][INFO]   "+"Be Ready to Initial connection to AMF ...")
	print(CurrentPath+":27   "+"[eNB][INFO]   "+"call AMF amfeNBInterface operation with MsgType(eNBConnect2AMF) and http method(post)")
	print(CurrentPath+":28   "+"[eNB][INFO]   "+"post http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface")
	Connect2AMF = "http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface"
	eNBInfo = {"ID":sys.argv[1],"MCC":"208","MNC":"93","TAC":"01","MsgType":"eNBConnect2AMF"}
	r1 = requests.post(Connect2AMF, data=eNBInfo)
	ret = b'"eNBConnect2AMFSuccess"\n'
	if ret == r1.content :
		print(CurrentPath+":34   "+"[eNB][INFO]   "+(r1.content).decode())
		print(CurrentPath+":35   "+"[UE][INFO]   "+"Be Ready to initial connection to AMF via eNB ...")
		print(CurrentPath+":36   "+"[UE][INFO]   "+"call AMF amfeNBInterface operation with MsgType(UEConnect2AMF) and http method(post)")
		print(CurrentPath+":37   "+"[UE][INFO]   "+"post http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface")
		UEConnect2AMFViaeNB = "http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface"
		UEConnectionInfo = {"eNBID":sys.argv[1],"MsgType":"UEConnect2AMF"}
		r2 = requests.post(UEConnect2AMFViaeNB,data=UEConnectionInfo)
		ret = b'"UEConnected2AMFSuccess"\n'
		if ret == r2.content :
			print(CurrentPath+":43   "+"[UE][INFO]   "+(r2.content).decode())
			print(CurrentPath+":44   "+"[UE][INFO]   "+"Be Ready to registe to AMF ...")
			print(CurrentPath+":45   "+"[UE][INFO]   "+"call AMF amfeNBInterface operation with MsgType(UEReqRigster) and http method(post)")
			print(CurrentPath+":46   "+"[UE][INFO]   "+"post http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface")
			UEReqRigster = "http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface"
			UEInfo = {"imsi":sys.argv[2],"msisdn":"32435235366","key":"8baf473f2f8fd09487cccbd7097c6863","opc":"e734f8734007d6c5ce7a0508809e7e9c","MsgType":"UEReqRigstr","ueListenPort":enp0s3Ip+":"+sys.argv[3]}
			r3 = requests.post(UEReqRigster,data=UEInfo)
			ret = b'"UERigister2AMFSuccess"\n'
			if ret == r3.content :
				print(CurrentPath+":52   [UE][INFO]   "+(r3.content).decode())
				print(CurrentPath+":53   [UE][INFO]   "+"response AMF Identity Request")
				print(CurrentPath+":54   "+"[UE][INFO]   "+"call AMF amfeNBInterface operation with MsgType(IdentityRsp) and http method(post)")
				print(CurrentPath+":55   "+"[UE][INFO]   "+"post http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface")
				IdentityRsp = "http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface"
				RspMsg = {"PEI":"2769169126891","MsgType":"IdentityRsp"}
				r4 = requests.post(IdentityRsp,data=RspMsg)
				if r4.status_code == 200:
					print(CurrentPath+":60   [UE][INFO]   "+"IdentityRspSuccess")
					print(CurrentPath+":61   [UE][INFO]   "+"Be Ready to initial PDU SESSION ESTABILISHMENT REQUEST")
					print(CurrentPath+":62   "+"[UE][INFO]   "+"call AMF amfeNBInterface operation with MsgType(PDUSessionEstabilishReq) and http method(post)")
					print(CurrentPath+":63   "+"[UE][INFO]   "+"post http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface")
					PDUSessionEstabilishReq = "http://192.168.1.109:5001/namf-comm/v1/amfeNBInterface"
					NASMsg = {"imsi":sys.argv[2],"PDUSessionID":"10","RequestType":"InitialRequest","PDUType":"IPv4v6","MsgType":"PDUSessionEstabilishReq"}
					r5 = requests.post(PDUSessionEstabilishReq,data=NASMsg)
                                	#ret = b'"PDUSessionEstabilishmentAccept"\n'
                                	#if ret == r5.content :
                                	#       print("[UE][INFO]   PDUSessionEstabilishmentAccept")
                                	#else:
                                	#       print("[UE][ERROR]  PDUSessionEstabilishmentNotAccept")
                                	#create_app().run(port=5555,debug=True)
				else :
					print(CurrentPath+":74   [UE][ERROR]  "+"IdentityRspFailure")
			else :
				print(CurrentPath+":76   [UE][ERROR]  "+(r3.content).decode())
		else :
			print(CurrentPath+":78   [UE][ERROR]  "+(r2.content).decode())
	else :
		print(CurrentPath+":68   "+"[eNB][ERROR]   "+(r1.content).decode())


#def running():
#	global enp0s3Ip
#	create_app().run(host=enp0s3Ip,port=int(sys.argv[3]))

print(CurrentPath+":106   [VM][INFO]   "+"config enp0s3 ip")
print(CurrentPath+":107   [VM][INFO]   "+"sudo dhclient enp0s3")
p = subprocess.Popen('sudo dhclient enp0s3',shell=True)
print(CurrentPath+":109   [enp0s3][ip] "+get_ip_address('enp0s3'))
enp0s3Ip = get_ip_address('enp0s3')
#t = Thread(target = running)
#t.start()
t = Thread(target = InitialReq,args=())
t.start()
#print("parameter number: "+str(len(sys.argv)))
#print("parameters :"+str(sys.argv))
#print(sys.argv[1])
#signal.signal(signal.SIGINT,quit)
#InitialReq()
#t = Thread(target = running)
#t.start
create_app().run(host='0.0.0.0',port=int(sys.argv[3]))





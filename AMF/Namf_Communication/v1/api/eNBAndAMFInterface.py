# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
import requests
from flask import request, g

from flask_restful import Resource,reqparse
from .. import logs

parser = reqparse.RequestParser()
##parse eNB Infos
parser.add_argument('MCC')
parser.add_argument('MNC')
parser.add_argument('TAC')
parser.add_argument('ID')
##parse UE eNB ID
parser.add_argument('eNBID')
##parse UE sim card infos
parser.add_argument('imsi')
parser.add_argument('msisdn')
parser.add_argument('key')
parser.add_argument('opc')
parser.add_argument('PEI')
##parse NASMsg
parser.add_argument('PDUSessionID')
parser.add_argument('RequestType')
parser.add_argument('PDUType') 
##parse MsgType
parser.add_argument('MsgType')
##parse ToAmfANInterface
parser.add_argument('AllocatedUEIp')
parser.add_argument('CNTunnelID')
parser.add_argument('UPFURI')
##global eNB parameters
MCC_VALID = "208"
MNC_VALID = "93"
TAC_VALID = "01"
##parse parameters of SMContext 
parser.add_argument('DeregistrationType')
parser.add_argument('AccessType')
#eNB Collections
#eNB Collections
eNBCollection = []

#Log infos
info = "|--------------------------------------------------------------|\n"\
      +"|                       eNB infos table                        |\n"\
      +"|--------------|---------------|---------------|---------------|\n"\
      +"|       ID     |      MCC      |      MNC      |      TAC      |\n"\
      +"|--------------|---------------|---------------|---------------|\n" 


from threading import Thread
def N2PDUSessionReq(args):
	print("\n\n[AMF][INFO]   "+"AMF PREPARE PDU SESSION ESTABILISHMENT REQ MSG ...")
	logs.s1uBearer += 1
	stcs = logs.info+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +"|----------------|-----------------|-----------------|-----------------|\n"
	print(stcs)
	print("[AMF][INFO]   "+"s1uBearer has been created successfully")
	UEURI = "http://127.0.0.1:5555/nue/v1/fromamfside"
	Msg2UE = {"AllocatedUEIp":args['AllocatedUEIp'],"UPFURI":args['UPFURI'],"CNTunnelID":args['CNTunnelID'],"imsi":args['imsi'],"status":"PDUSessionEstabilishmentReqAccept"}
	r = requests.post(UEURI,data=Msg2UE)
	#logs.s1uBearer += 1
	#stcs = logs.info+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
        #                +"|----------------|-----------------|-----------------|-----------------|\n"
	#print(stcs)
	#print("[AMF][INFO]   "+"s1uBearer has been created successfully")


class INTERFACEeNBSide(Resource):

    global info

    def __init__(self):
        self.info = info

    def post(self):
        global info,MCC_VALID,MNC_VALID,TAC_VALID,eNBCollection
        args = parser.parse_args()
        MsgType = args['MsgType']
        if operator.eq(MsgType,"eNBConnect2AMF"):
        	ID = args['ID']
        	MCC = args['MCC']
        	MNC = args['MNC']
        	TAC = args['TAC']
        	if not operator.eq(MCC_VALID,MCC):
            		return "BAD MCC"
        	elif not operator.eq(MNC_VALID,MNC):
            		return "BAD MNC"
        	elif not operator.eq(TAC_VALID,TAC):
            		return "BAD TAC"
        	#return "eNBConnect2AMFSuccess"
        	self.info += ("|     "+ID+"    "+"|      "+MCC+"      "+"|     "+"    "+MNC+"    "+"|       "+"    "+TAC+"   "+"|     "+"\n")\
                     +"|--------------|---------------|---------------|---------------|\n"
        	if len(eNBCollection)==0:
        		eNB = {'ID':ID,'MCC':MCC,'MNC':MNC,'TAC':TAC}
        		eNBCollection.append(eNB)
        		logs.eNBConnected+=1
        		print(self.info)
        		info = self.info
        		print("\n\n\n\n")
        	else :
        		for i in range(len(eNBCollection)):
        			eNB = {'ID':ID,'MCC':MCC,'MNC':MNC,'TAC':TAC}
        			if eNBCollection[i]['ID']==eNB['ID']:
        				break
       				elif i==len(eNBCollection)-1:
        				eNBCollection.append(eNB)
        				logs.eNBConnected+=1
        				print(self.info)
        				info = self.info
        				print("\n\n\n\n")
        	stcs = logs.info+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +"|----------------|-----------------|-----------------|-----------------|\n"
        	print(stcs)
        	return "eNBConnect2AMFSuccess"
        elif operator.eq(MsgType,"UEConnect2AMF"):
        	eNBID = args['eNBID']
        	if len(eNBCollection) == 0:
        		print("\n[AMF][ERROR]   "+"no eNB active in AMF\n")
        		return "NoeNBActiveInAMF"
        	for i in range(len(eNBCollection)):
        		if eNBCollection[i]['ID'] == eNBID:
        			logs.UEConnected += 1
        			stcs = logs.info+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +"|----------------|-----------------|-----------------|-----------------|\n"
        			print(stcs)
        			return "UEConnected2AMFSuccess"
        		elif i == len(eNBCollection)-1:
        			print("[AMF][ERROR]   "+"no eNB corresponding to UE eNBID")
        			return "NoeNBCorrespond2UEeNBID"
        elif operator.eq(MsgType,"UEReqRigstr"):
        	print("\n\n[AMF][INFO]   POST http://127.0.0.1/namf-comm/v1/ue-contexts/"+args['imsi']+"/transfer  200-")
        	print("[AMF][INFO]   "+"AMF COMMUNICATION UECONTEXT TRANSFER SUCCESS")
        	print("[AMF][INFO]   "+"BEGIN AUTHENTICATION PROCEDURE...")
        	print("[AMF][INFO]   "+"SEND UE SIM CARD INFOS TO AUSF...\n")
        	SendUEMsgToAUSF = "http://127.0.0.1:5020/nausf-ueAuth/v1/authenticate"
        	UEInfo = {"imsi":args['imsi'],"msisdn":args['msisdn'],"key":args['key'],"opc":args['opc']}
        	r = requests.post(SendUEMsgToAUSF,data=UEInfo)
        	ret = b'"UEAuthSuccess"\n'
        	if ret == r.content :
        		logs.UEAttached += 1
        		stcs = logs.info+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +"|----------------|-----------------|-----------------|-----------------|\n"
        		print(stcs)
        		print("[AMF][INFO]   "+(r.content).decode())
        		print("[AMF][INFO]   "+"PATCH http://127.0.0.1/namf-comm/v1/ue-contexts/"+args['imsi']+"  200-\n")
        		print("[AMF][INFO]   "+"IdentityRequest...")
        		return "UERigister2AMFSuccess"
        	else :
        		print("[AMF][ERROR]  "+(r.content).decode())
        		return "UERigister2AMFFailure"
        elif operator.eq(MsgType,"IdentityRsp"):
        	print("\n\n[AMF][INFO]   "+"IdentityResponseFromUE")
        	print("[AMF][INFO]   "+"UE PEI : "+args['PEI']+"\n\n")
        	return None,200
        elif operator.eq(MsgType,"PDUSessionEstabilishReq"):
        	print("\n\n[AMF][INFO]   "+"RecvPDUSessionEstabilishReqFromUE")
        	print("[AMF][INFO]   "+"Choosing SMF ...")
        	print("[AMF][INFO]   "+"sending SmContextCreateData to SMF to Create PDUSessionContext ...")
        	PDUSessionCreateSMContextReq = "http://127.0.0.1:5005/nsmf-pdusession/v1/sm-contexts"
        	SmContextCreateData = {"imsi":args['imsi'],"PDUSessionID":args['PDUSessionID'],"RequestType":args['RequestType'],"PDUType":args['PDUType']}
        	r = requests.post(PDUSessionCreateSMContextReq,data=SmContextCreateData)
       		if r.status_code == 201:
        		print("[AMF][INFO]   "+"SmContextCreatedData")
        		print("[AMF][INFO]   "+"SmContextCreatedData:  "+(r.content).decode()+"\n\n")
        	else :
        		print("[AMF][INFO]   "+"SmContextCreateError\n\n")
        elif operator.eq(MsgType,"ToAmfANInterface"):
        	t = Thread(target = N2PDUSessionReq,args=(args,))
        	t.start()
        	t.join()
        	return None,200
        	#print("[AMF][INFO]   "+"AMF PREPARE PDU SESSION ESTABILISHMENT REQ MSG ...")
        	#UEURI = "http://127.0.0.1:5555/nue/v1/fromamfside"
        	#Msg2UE = {"AllocatedUEIp":args['AllocatedUEIp'],"UPFURI":args['UPFURI'],"CNTunnelID":args['CNTunnelID'],"imsi":args['imsi'],"status":"PDUSessionEstabilishmentReqAccept"}
        	#r = requests.post(UEURI,data=Msg2UE)
        	#logs.s1uBearer += 1
        	#stcs = logs.info+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                #        +"|----------------|-----------------|-----------------|-----------------|\n"
       		#print(stcs)
        	
        elif operator.eq(MsgType,"UEInitialDeregistrationReq"):
        	print("[AMF][INFO]   "+"Receive UE Initial Deregistration Request")
        	ReleaseSMContextReq2SMF = "http://127.0.0.1:5005/nsmf-pdusession/v1/sm-contexts/"+args['imsi']+"/release"
        	r = requests.post(ReleaseSMContextReq2SMF,data=args)	
       		if r.status_code == 204:
        		print("[AMF][INFO]   "+"Release SMContext about "+args['imsi']+" success")
        		print("[AMF][INFO]   "+"SMF Response 204 No Content")
        		logs.s1uBearer -= 1
        		logs.UEAttached -= 1
        		logs.UEConnected -= 1
        		stcs = logs.info+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +"|----------------|-----------------|-----------------|-----------------|\n"
       			print(stcs)
        		return "DeregistrationAccept"
       		else:
        		print("[AMF][ERROR]  "+"Release SMContext about "+args['imsi']+" failure")
        		return "DeregistrationNotAccept"
        
        elif operator.eq(MsgType,"ReleaseANReq"):
        	print("[AMF][INFO]   "+"Receive Release AN Request")
        	logs.eNBConnected -= 1
        	stcs = logs.info+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +"|----------------|-----------------|-----------------|-----------------|\n"
        	print(stcs)
        	for i in range(len(eNBCollection)):
        		if operator.eq(args['eNBID'],eNBCollection[i]['ID']):
        			#self.info -= ("|     "+eNBCollection[i]['ID']+"    "+"|      "+eNBCollection[i]['MCC']+"      "+"|     "+"    "+eNBCollection[i]['MNC']+"    "+"|       "+"    "+eNBCollection[i]['TAC']+"   "+"|     "+"\n")\
                     #+"|--------------|---------------|---------------|---------------|\n"
        			#info = self.info
        			eNBCollection.remove(eNBCollection[i])
        			break
        	#print(self.info)
        	return None,200
        
        
        

# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
#from . import Resource
#from .. import schemas
from flask_restful import Resource,reqparse

from .. import logs


parser = reqparse.RequestParser()
parser.add_argument('imsi')

parser.add_argument('tmsi')

parser.add_argument('key')
parser.add_argument('opc')

MCC_VALID = "208"
MNC_VALID = "93"
TAC_VALID = "1"

info = "                                                                                         "+"|----------------------------------------------------------------------|\n"\
      +"                                                                                         "+"|                               statistics                             |\n"\
      +"                                                                                         "+"|----------------|-----------------|-----------------|-----------------|\n"\
      +"                                                                                         "+"  eNB connected     ue connected       ue attached        s1u bearer    \n"\
      +"                                                                                         "+"|----------------|-----------------|-----------------|-----------------|\n" 

def display(eNBInfo):
    print(eNBInfo)
    #print("|--------------|---------------|---------------|---------------|")
    #print("     ID            MCC             MNC             TAC")
    #print("|--------------|---------------|---------------|---------------|")
    #print("    "+ID+"    ","    "+MCC+"    ","       "+MNC+"      ","       "+TAC+"      ")
class AMFOPT1(Resource):
    global info
    def __init__(self):
        self.info = info
        #print("hello")
    def get(self):
        data={'name':"hello",'passwd':"world"}
        return data,200

    def post(self):
        #global info,MCC_VALID,MNC_VALID,TAC_VALID
        #print("world")
        #print(info)
        args = parser.parse_args()
        print(args)
        logs.UEConnected+=1
        url="http://127.0.0.1:5007/Nudm-UEAuthentication/v1/ueAuth"
        r = requests.post(url, data=args)
        print (r.status_code)
        print ((r.content))
        authOk = b'"auth_ok"\n'
        if r.content == authOk:
        	logs.UEAttached+=1
        stcs = logs.info+"                                                                                         "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +"                                                                                         "+"|----------------|-----------------|-----------------|-----------------|\n"
        print(stcs) 
        return "attach_success"
        #ID = args['ID']
        #MCC = args['MCC']
        #MNC = args['MNC']
        #TAC = args['TAC']
        #print(not operator.eq(MCC_VALID,MCC))
        #if not operator.eq(MCC_VALID,MCC):
        #    return "BAD MCC"
        #elif not operator.eq(MNC_VALID,MNC):
        #    return "BAD MNC"
        #elif not operator.eq(TAC_VALID,TAC):
        #    return "BAD TAC"
        #self.info += "                                                                                         "+("    "+ID+"    "+"       "+MCC+"      "+"      "+MNC+"        "+"        "+TAC+"      "+"\n")\
        #             +"                                                                                         "+"|--------------|---------------|---------------|---------------|\n"
        #info = self.info 
        #display(logs.info)

        
        
        

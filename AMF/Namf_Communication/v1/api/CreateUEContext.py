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
class CreateUECtx(Resource):
    global info
    def __init__(self):
        self.info = info
        #print("hello")
    def get(self):
        data={'name':"hello",'passwd':"world"}
        return data,200

    def post(self):

        url="http://127.0.0.1:5005/Nsmf-PDUSession/v1/pdusession_create"
        r = requests.post(url, data="")
        print (r.status_code)
        print ((r.content))
        PDUSessionCreateOk = b'"pdusession_create_ok"\n'
        if r.content == PDUSessionCreateOk: 
        	print("PDUSession Create successfully!")
        	url="http://127.0.0.1:5005/Nsmf-PDUSession/v1/pdusession_create_smcontext"
        	r = requests.post(url, data="")
        	print(r.status_code)
       		print(r.content)
       		PDUSessionCreateSMCtxOk = b'"pdusession_create_smctx_ok"\n'
        	if r.content == PDUSessionCreateSMCtxOk:
        		print("PDUSession Create SMCtx successfully!")
        		logs.s1uBearer+=1
        		stcs = logs.info+"                                                                                         "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +"                                                                                         "+"|----------------|-----------------|-----------------|-----------------|\n"
        		print(stcs)
        	
        
        
        

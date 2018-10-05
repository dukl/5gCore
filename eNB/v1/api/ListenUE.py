# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
#from . import Resource
#from .. import schemas
from flask_restful import Resource,reqparse


parser = reqparse.RequestParser()
parser.add_argument('imsi')
parser.add_argument('tmsi')
parser.add_argument('key')
parser.add_argument('opc')

MCC_VALID = "208"
MNC_VALID = "93"
TAC_VALID = "1"

info = "                                                                                         "+"|--------------------------------------------------------------|\n"\
      +"                                                                                         "+"|                       eNB infos table                        |\n"\
      +"                                                                                         "+"|--------------|---------------|---------------|---------------|\n"\
      +"                                                                                         "+"        ID            MCC             MNC             TAC\n"\

def display(eNBInfo):
    print(eNBInfo)
    #print("|--------------|---------------|---------------|---------------|")
    #print("     ID            MCC             MNC             TAC")
    #print("|--------------|---------------|---------------|---------------|")
    #print("    "+ID+"    ","    "+MCC+"    ","       "+MNC+"      ","       "+TAC+"      ")
class LIUE(Resource):
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
        url="http://127.0.0.1:5001/Namf-Communication/v1/amf_operation_1"
        args = parser.parse_args()
        payload = {'imsi':args['imsi'],'tmsi':args['tmsi'],'key':args['key'],'opc':args['opc']}
        r = requests.post(url, data=payload)
        print (r.status_code)
        print (r.content)
        attach_success = b'"attach_success"\n'
        if r.content == attach_success:
        	url="http://127.0.0.1:5001/Namf-Communication/v1/create_ue_ctx"
        	r = requests.post(url,data="")
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
        #display(self.info)

        
        
        

# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
#from . import Resource
#from .. import schemas
from flask_restful import Resource,reqparse


parser = reqparse.RequestParser()

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
class UEDATATRANSFER(Resource):
    global info
    def __init__(self):
        self.info = info
        #print("hello")
    def get(self):
        data={'name':"hello",'passwd':"world"}
        return data,200

    def post(self):
        url="http://127.0.0.1:5012/Nupf-DataTransfer/v1/uedata"
        args = parser.parse_args()
        print(args)
        #payload = {'imsi':args['imsi'],'tmsi':args['tmsi'],'key':args['key'],'opc':args['opc']}
        r = requests.post(url, data=args)
        print (r.status_code)
        print (r.content)
        #attach_success = b'"attach_success"\n'
        #if r.content == attach_success:
        #	url="http://127.0.0.1:5001/Namf-Communication/v1/create_ue_ctx"
        #	r = requests.post(url,data="")

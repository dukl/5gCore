# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
#from . import Resource
#from .. import schemas
from flask_restful import Resource,reqparse

from sqlalchemy import Column, String, create_engine,LargeBinary
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

#from .. import users
#from users import Users

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
      +"                                                                                         "+"|--------------|---------------|---------------|---------------|\n" 

def display(eNBInfo):
    print(eNBInfo)
    #print("|--------------|---------------|---------------|---------------|")
    #print("     ID            MCC             MNC             TAC")
    #print("|--------------|---------------|---------------|---------------|")
    #print("    "+ID+"    ","    "+MCC+"    ","       "+MNC+"      ","       "+TAC+"      ")
class SMContext(Resource):
    global info
    def __init__(self):
        self.info = info
        #print("hello")
    def get(self):
        data={'name':"hello",'passwd':"world"}
        return data,200

    def post(self):
        #print("world")
        url="http://127.0.0.1:5012/Nupf-DataTransfer/v1/upConfig"
        r = requests.post(url, data="")
        print (r.status_code)
        print ((r.content))
        ConfigOk = b'"config_ok"\n'
        if r.content == ConfigOk:
        	print("UP Config successfully!")
        return "pdusession_create_smctx_ok"

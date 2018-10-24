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
class UEBearer(Resource):
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
        #url="http://127.0.0.1:5000/Namf-Communication/v1/amf_operation_1"
        args = parser.parse_args()
        print(args)
        #engine = create_engine('mysql+mysqlconnector://root:linux@localhost:3306/oai_db?charset=utf8')
        #DBSession = sessionmaker(bind=engine)
        # 创建session对象:
        #session = DBSession()
        #user = session.query(users.Users).filter(users.Users.imsi=='208930000000001').one()
        #print('type:',type(user))
        #print('imei:',type(user.imei))
        #print('OPc:',type(user.OPc))
        #opc_str = args['opc']
        #opc = bytes().fromhex(opc_str)
        #print((opc))
        #if user.OPc == opc:
        #	print('hhhhhh')
        #	return "auth_ok"
        #else:
        #	print('eeeeee');
        #	return "auth_error"
        
        #payload = {'imsi':args['imsi'],'tmsi':args['tmsi'],'key':args['key'],'opc':args['opc']}
        #r = requests.post(url, data=payload)
        #print (r.status_code)
        #print (r.content)
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

        
        
       #pass 

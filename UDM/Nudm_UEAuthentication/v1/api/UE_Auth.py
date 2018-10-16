# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
import json
from flask_restful import Resource,reqparse

from sqlalchemy import Column, String, create_engine,LargeBinary
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from .. import tables

parser = reqparse.RequestParser()
parser.add_argument('imsi')
parser.add_argument('key')
parser.add_argument('opc')

CurrentPath = "~/5GCORE/UDM/Nudm_UEAuthentication/v1/api/UE_Auth.py"

class UEAUTH(Resource):
    global info
    def __init__(self):
    	pass 
    def post(self):
        args = parser.parse_args()
        print(CurrentPath+":29   [UDM][INFO]   "+"receive AUSF get mysql infos with imsi("+args['imsi']+")")
        print(CurrentPath+":30   [UDM][INFO]   "+"create engine to connect mysql")
        engine = create_engine('mysql+mysqlconnector://root:linux@localhost:3306/oai_db?charset=utf8')
        DBSession = sessionmaker(bind=engine)
        # 创建session对象:
        session = DBSession()
        users = session.query(tables.Users).filter(tables.Users.imsi==args['imsi']).one()
        print(CurrentPath+":36   [UDM][INFO]   "+"infos about imsi("+args['imsi']+") in mysql as following")
        print("\n\n|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("|                                                                       mysql user infos where imsi = "+args['imsi']+"                                                                 |")
        print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("|        imsi        |         msisdn       |         imei        | mmeidentity_idmmeidentity |                      key                    |                     OPc                 |")
        print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")        
        print("|   "+users.imsi+"  |       "+users.msisdn+"    |    "+users.imei+"   |                 "+str(users.mmeidentity_idmmeidentity)+"         |        "+"0x8baf473f2f8fd09487cccbd7097c6862"+"   |    "+"0xe734f8734007d6c5ce7a0508809e7e9c"+"   |")       
        print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n\n") 
        data = {'imsi':users.imsi,'msisdn':users.msisdn,'key':'8baf473f2f8fd09487cccbd7097c6862','opc':'e734f8734007d6c5ce7a0508809e7e9c'}        
        return (json.dumps(data)) 

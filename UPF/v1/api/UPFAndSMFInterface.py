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

from .. import status
parser = reqparse.RequestParser()
parser.add_argument('CNTunnelID')
parser.add_argument('imsi')
parser.add_argument('MsgType')
parser.add_argument('DeregistrationType')
parser.add_argument('AccessType')


CurrentPath = "~/5GCORE/UPF/v1/api/UPFAndSMFInterface.py"


class INTERFACE(Resource):

    def __init__(self):
    	pass

    def post(self):
    	args = parser.parse_args()
    	if operator.eq(args['MsgType'],"N4SessionEstabilishmentReq"):
    		print(CurrentPath+":34   [UPF][INFO]   "+"UPF RECEIVES N4 SESSION ESTABILISHMENT REQUEST FROM SMF")
    		print(CurrentPath+":35   [UPF][INFO]   "+"UPF handling N4 SESSION ESTABILISHMENT REQUEST ")
    		N4SessionEstabilishmentRsp = {"imsi":args['imsi'],"CNTunnelID":args['CNTunnelID'],"UPFURI":"http://127.0.0.1:5012/nupf/v1/eNBUpfInterface"}
    		return json.dumps(N4SessionEstabilishmentRsp),200
    	elif operator.eq(args['MsgType'],"UEInitialDeregistrationReq"):
    		print(CurrentPath+":39   [UPF][INFO]   "+"UPF Release N4 Session success and delete SMContext")
    		return None,200
    	

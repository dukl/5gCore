# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
from flask_restful import Resource,reqparse

from sqlalchemy import Column, String, create_engine,LargeBinary
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

parser = reqparse.RequestParser()
parser.add_argument('CNTunnelID')
parser.add_argument('imsi')
parser.add_argument('MsgType')
parser.add_argument('DeregistrationType')
parser.add_argument('AccessType')


class SMContextRelease(Resource):

    def post(self,smContextRef):
    	args = parser.parse_args()
    	print("[SMF][INFO]   "+"Receive deregistration req")
    	N4SessionReleaseReq = "http://127.0.0.1:5012/nupf/v1/UpfSmfInterface"
    	r = requests.post(N4SessionReleaseReq, data=args)
    	if r.status_code == 200:
    		print("[SMF][INFO]   "+"Release SMContext success")
    		return None,204
    	else:
     		print("[SMF][ERROR]  "+"No handle for SMF Release SMContext request")
  

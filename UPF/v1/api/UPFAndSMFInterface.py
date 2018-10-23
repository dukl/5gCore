# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
import json
import subprocess
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
parser.add_argument('CreateDataConnection')



CurrentPath = "~/5GCORE/UPF/v1/api/UPFAndSMFInterface.py"


class INTERFACE(Resource):

    def __init__(self):
    	pass

    def post(self):
    	args = parser.parse_args()
    	if operator.eq(args['MsgType'],"N4SessionEstabilishmentReq"):
    		print(CurrentPath+":36   [UPF][INFO]   "+"UPF RECEIVES N4 SESSION ESTABILISHMENT REQUEST FROM SMF")
    		print(CurrentPath+":37   [UPF][INFO]   "+"UPF handling N4 SESSION ESTABILISHMENT REQUEST ")
		if operator.eq(args['CreateDataConnection'],"TRUE"):
			print(CurrentPath+":39   [UPF][INFO]   "+"Config bridge to create data connection")
			#print(CurrentPath+":40   [UPF][INFO]   "+"sudo brctl addbr br0")
			#p = subprocess.Popen('sudo brctl addbr br0',shell=True,close_fds=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
			#p.stdin.write(b'"123\n"')
			#p.wait()
			#print(CurrentPath+":45   [UPF][INFO]   "+"sudo ip tuntap add dev port mode tap")
			#p = subprocess.Popen('sudo ip tuntap add dev port mode tap',shell=True)
			#print(CurrentPath+":47   [UPF][INFO]   "+"sudo ifconfig port up")
			#p = subprocess.Popen('sudo ifconfig port up',shell=True)
			#print(CurrentPath+":49   [UPF][INFO]   "+"sudo brctl addif br0 port")
			#p = subprocess.Popen('sudo brctl addif br0 port',shell=True)
			#print(CurrentPath+":51   [UPF][INFO]   "+"sudo brctl addif br0 enp3s0")
			#p = subprocess.Popen('sudo brctl addif br0 enp3s0',shell=True)
			print(CurrentPath+":53   [UPF][INFO]   "+"sudo ifconfig data up")
			p = subprocess.Popen('sudo ifconfig data up',shell=True)
			print(CurrentPath+":55   [UPF][INFO]   "+"sudo brctl addif br0 data")
			p = subprocess.Popen('sudo brctl addif  br0 data',shell=True)
    		N4SessionEstabilishmentRsp = {"imsi":args['imsi'],"CNTunnelID":args['CNTunnelID'],"UPFURI":"http://127.0.0.1:5012/nupf/v1/eNBUpfInterface"}
    		return json.dumps(N4SessionEstabilishmentRsp),200
    	elif operator.eq(args['MsgType'],"UEInitialDeregistrationReq"):
    		print(CurrentPath+":60   [UPF][INFO]   "+"UPF Release N4 Session success and delete SMContext")
    		print(CurrentPath+":61   [UPF][INFO]   "+"UPF delete configuration")
    		print(CurrentPath+":62   [UPF][INFO]   "+"sudo brctl delif br0 data")
    		p = subprocess.Popen('sudo brctl delif br0 data',shell=True)
    		#print(CurrentPath+":64   [UPF][INFO]   "+"sudo brctl delif br0 enp3s0")
    		#p = subprocess.Popen('sudo brctl delif br0 enp3s0',shell=True)
    		#print(CurrentPath+":66   [UPF][INFO]   "+"sudo ip tuntap del dev port mode tap")
    		#p = subprocess.Popen('sudo ip tuntap del dev port mode tap',shell=True)
    		#print(CurrentPath+":68   [UPF][INFO]   "+"sudo ifconfig br0 down")
    		#p = subprocess.Popen('sudo ifconfig br0 down',shell=True)
        	#p.wait()
    		#print(CurrentPath+":70   [UPF][INFO]   "+"sudo brctl delbr br0")
    		#p = subprocess.Popen('sudo brctl delbr br0',shell=True)
    		#print(CurrentPath+":72   [UPF][INFO]   "+"sudo dhclient enp3s0")
    		#p = subprocess.Popen('sudo dhclient enp3s0',shell=True)
    		return None,200
    	

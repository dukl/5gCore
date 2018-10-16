# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g

from flask_restful import Resource,reqparse
from .. import logs

import requests

parser = reqparse.RequestParser()
parser.add_argument('AllocatedUEIp')
parser.add_argument('CNTunnelID')
parser.add_argument('UPFURI')

CurrentPath = "~/5GCORE/AMF/Namf_Communication/v1/api/n1n2message.py"

##create thread
from threading import Thread
def AMFNotifyToAN(args,ueContextID):
	print(CurrentPath+":21   [AMF][INFO]   "+"AMF receives SMF INFOS NOTIFY")
	print(CurrentPath+":22   [AMF][INFO]   "+"sendind UE Allocated infos to AMF amfeNBInterface")
	print(CurrentPath+":23   [AMF][INFO]   "+"post http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface")
	ToAmfANInterface = "http://127.0.0.1:5001/namf-comm/v1/amfeNBInterface"
	Msg = {"MsgType":"ToAmfANInterface","AllocatedUEIp":args['AllocatedUEIp'],"CNTunnelID":args['CNTunnelID'],"UPFURI":args['UPFURI'],"imsi":str(ueContextID)}
	r = requests.post(ToAmfANInterface,data=Msg)
	pass

class N1N2MSG(Resource):

    def post(self,ueContextID):
    	args = parser.parse_args()
    	t = Thread(target = AMFNotifyToAN,args=(args,ueContextID,))
    	t.start()    	
    	return None,200

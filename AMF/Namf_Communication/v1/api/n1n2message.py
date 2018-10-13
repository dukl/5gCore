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

##create thread
from threading import Thread
def AMFNotifyToAN(args,ueContextID):
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

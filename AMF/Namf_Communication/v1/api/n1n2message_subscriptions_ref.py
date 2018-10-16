# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g

from flask_restful import Resource,reqparse
parser = reqparse.RequestParser()
parser.add_argument('MCC')

class ONEN1N2MSGSUB(Resource):

    def put(self,ueContextID,subscriptionId):
    	args = parser.parse_args()
    	print(ueContextID,subscriptionId)

    def delete(self,ueContextID,subscriptionId):
    	print(ueContextID,subscriptionId)
    	pass

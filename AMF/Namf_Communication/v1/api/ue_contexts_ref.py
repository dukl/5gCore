# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g

from flask_restful import Resource,reqparse
parser = reqparse.RequestParser()
parser.add_argument('MCC')

class ONEUECONTEXT(Resource):

    def post(self,ueContextID):
    	print(ueContextID)
    	args = parser.parse_args()
        return "visit AMF Communication service operation(http method: post) : /namf-comm/v1/ue-contexts/<int:ueContextID>"

    def patch(self,ueContextID):
    	print("patch method")
	return "visit AMF Communication service operation(http method: patch) : /namf-comm/v1/ue-contexts/<int:ueContextID>"
    	pass

    def put(self,ueContextID):
    	print("put method")
        return "visit AMF Communication service operation(http method: delete) : /namf-comm/v1/ue-contexts/<int:ueContextID>"
    	pass

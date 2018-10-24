# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g

from flask_restful import Resource,reqparse

parser = reqparse.RequestParser()
parser.add_argument('MCC')

class ProvideInfo(Resource):

    def get(self,ueContextID):
        args = parser.parse_args()
    	print("[AMF][INFO]   "+"AMF Receives request for Namf_MT service")
        return "visit AMF MT service operation(http method: get) : /namf-mt/v1/ue_contexts/<int:ueContextId>" 

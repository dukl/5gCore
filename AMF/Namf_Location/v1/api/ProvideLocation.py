# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
from flask_restful import Resource,reqparse

parser = reqparse.RequestParser()
parser.add_argument('imsi')


class PROVIDELOCATION(Resource):

    def post(self,ueContextId):
        args = parser.parse_args()
        print(args)
        #return "visit AMF Location service operation(http method: post) : /namf-loc/v1/ue-contexts/<int:ueContext>/provide"
    	LocationInfos = {"eNBID":"28192","MCC":"208","MNC":"93","TAC":"01"}    	
    	return "eNBInfosWithUEimsi"+str(ueContextId)+":"+str(LocationInfos)
        
        
        

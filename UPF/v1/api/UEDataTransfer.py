# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
#from . import Resource
#from .. import schemas
from flask_restful import Resource,reqparse

from sqlalchemy import Column, String, create_engine,LargeBinary
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

#from .. import users
#from users import Users
from .. import status
parser = reqparse.RequestParser()

def display(eNBInfo):
    print(eNBInfo)
    #print("|--------------|---------------|---------------|---------------|")
    #print("     ID            MCC             MNC             TAC")
    #print("|--------------|---------------|---------------|---------------|")
    #print("    "+ID+"    ","    "+MCC+"    ","       "+MNC+"      ","       "+TAC+"      ")
class DATATRANSFER(Resource):
    global info
    def __init__(self):
    	pass
        #self.info = info
        #print("hello")
    def get(self):
        data={'name':"hello",'passwd':"world"}
        return data,200

    def post(self):

    	if b'"upConfigOk"'==status.upStatus:
    		print("transfer data successfully!")
    		args = parser.parse_args()
    		print(args)
    	else:
    		print("up haven't configed successfully!")	

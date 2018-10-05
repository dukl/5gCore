# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g

#from . import Resource
#from .. import schemas
from flask_restful import Resource,reqparse
from .. import logs

parser = reqparse.RequestParser()
parser.add_argument('MCC')
parser.add_argument('MNC')
parser.add_argument('TAC')
parser.add_argument('ID')

MCC_VALID = "208"
MNC_VALID = "93"
TAC_VALID = "1"

eNBCollection = []



info = "                                                                                         "+"|--------------------------------------------------------------|\n"\
      +"                                                                                         "+"|                       eNB infos table                        |\n"\
      +"                                                                                         "+"|--------------|---------------|---------------|---------------|\n"\
      +"                                                                                         "+"|       ID     |      MCC      |      MNC      |      TAC      |\n"\
      +"                                                                                         "+"|--------------|---------------|---------------|---------------|\n" 

def display(eNBInfo):
    print(eNBInfo)
    #print("|--------------|---------------|---------------|---------------|")
    #print("     ID            MCC             MNC             TAC")
    #print("|--------------|---------------|---------------|---------------|")
    #print("    "+ID+"    ","    "+MCC+"    ","       "+MNC+"      ","       "+TAC+"      ")
class ENB(Resource):
    global info
    def __init__(self):
        self.info = info
        #print("hello")
    def get(self):
        data={'name':"hello",'passwd':"world"}
        return data,200

    def post(self):
        global info,MCC_VALID,MNC_VALID,TAC_VALID,eNBCollection
        #print("world")
        #print(info)
        args = parser.parse_args()
        print(args)
        ID = args['ID']
        MCC = args['MCC']
        MNC = args['MNC']
        TAC = args['TAC']
        #print(not operator.eq(MCC_VALID,MCC))
        if not operator.eq(MCC_VALID,MCC):
            return "BAD MCC"
        elif not operator.eq(MNC_VALID,MNC):
            return "BAD MNC"
        elif not operator.eq(TAC_VALID,TAC):
            return "BAD TAC"
        self.info += "                                                                                         "+("|   "+ID+"    "+"|      "+MCC+"      "+"|     "+"    "+MNC+"    "+"|       "+"    "+TAC+"   "+"|     "+"\n")\
                     +"                                                                                         "+"|--------------|---------------|---------------|---------------|\n"
        #info = self.info 
        if len(eNBCollection)==0:
        	eNB = {'ID':ID,'MCC':MCC,'MNC':MNC,'TAC':TAC}
        	eNBCollection.append(eNB)
        	logs.eNBConnected+=1
        	display(self.info)
        	info = self.info
        	print("\n\n\n\n")
        else :
        	for i in range(len(eNBCollection)):
        		eNB = {'ID':ID,'MCC':MCC,'MNC':MNC,'TAC':TAC}
        		if eNBCollection[i]['ID']==eNB['ID']:
        			break
       			elif i==len(eNBCollection)-1:
        			eNBCollection.append(eNB)
        			logs.eNBConnected+=1
        			display(self.info)
        			info = self.info
        			print("\n\n\n\n")
        stcs = logs.info+"                                                                                         "+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
                        +"                                                                                         "+"|----------------|-----------------|-----------------|-----------------|\n"
        display(stcs)
        return "connect_ok"

        
        
        

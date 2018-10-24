# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
from flask_restful import Resource,reqparse

parser = reqparse.RequestParser()
parser.add_argument('imsi')


class PROVIDELOCATION(Resource):

    def post(self,ueContextID):
        args = parser.parse_args()
        print(args)
        return "visit AMF Location service operation(http method: post) : /namf-loc/v1/ue-contexts/<int:ueContext>/provide"

        
        
        

# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g

from flask_restful import Resource,reqparse
parser = reqparse.RequestParser()
parser.add_argument('MCC')

class ONEUECONTEXTRELEASE(Resource):

    def post(self,ueContextID):
        args = parser.parse_args()
        return "visit AMF Communication service operation(http method: post) : /namf-comm/v1/ue-contexts/<int:ueContextID>/release"

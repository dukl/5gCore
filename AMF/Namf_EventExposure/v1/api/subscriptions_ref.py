# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g

from flask_restful import Resource,reqparse
parser = reqparse.RequestParser()
parser.add_argument('MCC')

class ONESUBSCRIPTION(Resource):

    def patch(self,subscriptionId):
        args = parser.parse_args()

    def delete(self,subscriptionId):
    	pass

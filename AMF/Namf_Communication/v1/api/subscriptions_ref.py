# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g

from flask_restful import Resource,reqparse
parser = reqparse.RequestParser()
parser.add_argument('MCC')

class ONESUBSCRIPTION(Resource):

    def delete(self,subscriptionId):
    	print(subscriptionId)
        return "visit AMF Communication service operation(http method: delete) : /namf-comm/v1/subscriptions/<int:subscriptionId>"
    	args = parser.parse_args()

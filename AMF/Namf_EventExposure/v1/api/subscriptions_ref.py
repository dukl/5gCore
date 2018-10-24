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
        return "visit AMF EventExposure service operation(http method: patch) : /namf-evts/v1/subscriptions/<int:subscriptionId> "

    def delete(self,subscriptionId):
        return "visit AMF EventExposure service operation(http method: delete) : /namf-evts/v1/subscriptions/<int:subscriptionId> "
    	pass

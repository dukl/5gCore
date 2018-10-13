# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
from flask_restful import Resource,reqparse

from sqlalchemy import Column, String, create_engine,LargeBinary
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from .. import status
parser = reqparse.RequestParser()
parser.add_argument('imsi')
parser.add_argument('payload')


class N3(Resource):

	def post(self):
		args = parser.parse_args()
		print("\n\n[UPF][DATA][IND][payload]:   "+str(args['payload'])+"\n\n")

	def delete(self):
		pass

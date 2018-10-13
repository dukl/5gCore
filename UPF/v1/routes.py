# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.UPFAndSMFInterface import INTERFACE
from .api.UPFAndANInterface import N3



routes = [
    dict(resource=INTERFACE, urls=['/UpfSmfInterface'], endpoint='UPFAndSMFInterface'),
    dict(resource=N3, urls=['/eNBUpfInterface'], endpoint='UPFAndANInterface'),


]

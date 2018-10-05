# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.PDUSessionCreate import PDUSession

from .api.PDUSessionCreateSMContext import SMContext


routes = [
    dict(resource=PDUSession, urls=['/pdusession_create'], endpoint='PDUSessionCreate'),
    
    dict(resource=SMContext, urls=['/pdusession_create_smcontext'], endpoint='PDUSessionCreateSMContext'),
    
]

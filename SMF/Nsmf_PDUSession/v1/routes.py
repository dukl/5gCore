# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.PDUSessionCreate import PDUSession

from .api.PDUSessionCreateSMContext import SMContextCreate

from .api.PDUSessionReleaseSMContext import SMContextRelease


routes = [
    dict(resource=PDUSession, urls=['/pdusession_create'], endpoint='PDUSessionCreate'),
    
    dict(resource=SMContextCreate, urls=['/sm-contexts'], endpoint='PDUSessionCreateSMContext'),
    
    dict(resource=SMContextRelease, urls=['/sm-contexts/<int:smContextRef>/release'], endpoint='PDUSessionReleaseSMContext'),
    
]

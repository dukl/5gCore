# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.eNBAndAMFInterface import INTERFACEeNBSide
from .api.n1n2message import N1N2MSG






routes = [
    dict(resource=INTERFACEeNBSide, urls=['/amfeNBInterface'], endpoint='eNBAndAMFInterface'),
    dict(resource=N1N2MSG, urls=['/<int:ueContextID>/n1-n2-messages'], endpoint='n1n2message'),


]

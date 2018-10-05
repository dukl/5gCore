# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.UPConfig import CONF

from .api.UEDataTransfer import DATATRANSFER


routes = [
    dict(resource=CONF, urls=['/upConfig'], endpoint='UPConfig'),

    dict(resource=DATATRANSFER, urls=['/uedata'], endpoint='UEDataTransfer'),

]

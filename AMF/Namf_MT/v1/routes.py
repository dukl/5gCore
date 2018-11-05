# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.ue_reachind import UEREACHIND
from .api.ProvideDomainSelectionInfo import ProvideInfo



routes = [
    dict(resource=UEREACHIND, urls=['/ue_contexts/<int:ueContextId>/ue_reachind'], endpoint='ue_reachind'),
    dict(resource=ProvideInfo, urls=['/ue_contexts/<int:ueContextId>'], endpoint='ProvideDomainSelectionInfo'),
]

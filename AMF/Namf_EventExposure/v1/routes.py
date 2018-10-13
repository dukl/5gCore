# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.eNB import ENB

from .api.UEActivityNotify import UEACTIVITYNOTIFY



routes = [
    dict(resource=ENB, urls=['/eNB'], endpoint='eNB'),

    dict(resource=UEACTIVITYNOTIFY, urls=['/ue_activity_notify'], endpoint='UEActivityNotify'),


]

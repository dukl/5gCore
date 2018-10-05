# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.eNB import ENB
from .api.amfOpt1 import AMFOPT1
from .api.amfOpt2 import AMFOPT2
from .api.CreateUEContext import CreateUECtx



routes = [
    dict(resource=ENB, urls=['/eNB'], endpoint='eNB'),

    dict(resource=AMFOPT1, urls=['/amf_operation_1'], endpoint='amfOpt1'),

    dict(resource=AMFOPT2, urls=['/amf_operation_2'], endpoint='amfOpt2'),

    dict(resource=CreateUECtx, urls=['/create_ue_ctx'], endpoint='CreateUEContext'),

]

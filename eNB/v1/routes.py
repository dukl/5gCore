# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.ListenUE import LIUE

from .api.UEDataTransfer import UEDATATRANSFER


routes = [
    dict(resource=LIUE, urls=['/ueConnect'], endpoint='listen_UE'),

    dict(resource=UEDATATRANSFER, urls=['/ue_data_transfer'], endpoint='UEDataTransfer'),

]

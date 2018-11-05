# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.subscriptions import SUBSCRIPTIONS
from .api.subscriptions_ref import ONESUBSCRIPTION




routes = [
    dict(resource=SUBSCRIPTIONS, urls=['/subscriptions'], endpoint='subscriptions'),
    dict(resource=ONESUBSCRIPTION, urls=['/subscriptions/<int:subscriptionId>'], endpoint='subscriptions-ref'),
]

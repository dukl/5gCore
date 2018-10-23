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
from .api.ue_contexts_ref import ONEUECONTEXT
from .api.ue_contexts_ref_release import ONEUECONTEXTRELEASE
from .api.ue_contexts_ref_assignEbi import ONEUECONTEXTASSIGNEBI
from .api.ue_contexts_ref_transfer import ONEUECONTEXTTRANSFER
from .api.ue_contexts import UECONTEXTS
from .api.n1n2message_subscriptions import N1N2MSGSUB
from .api.n1n2message_subscriptions_ref import ONEN1N2MSGSUB
from .api.subscriptions import SUBSCRIPTIONS
from .api.subscriptions_ref import ONESUBSCRIPTION
from .api.non_ue_n2_msg import NONUEN2MSG
from .api.non_ue_n2_msg_subscriptions import NONUEN2MSGSUB
from .api.non_ue_n2_msg_subscriptions_ref import ONENONUEN2MSGSUB


routes = [
    dict(resource=INTERFACEeNBSide, urls=['/amfeNBInterface'], endpoint='eNBAndAMFInterface'),
    dict(resource=N1N2MSG, urls=['/<int:ueContextID>/n1-n2-messages'], endpoint='n1n2message'),
    dict(resource=ONEUECONTEXT, urls=['/ue-contexts/<int:ueContextID>'], endpoint='ue-contexts-ref'),
    dict(resource=ONEUECONTEXTRELEASE, urls=['/ue-contexts/<int:ueContextID>/release'], endpoint='ue-contexts-ref-release'),
    dict(resource=ONEUECONTEXTASSIGNEBI, urls=['/ue-contexts/<int:ueContextID>/assignEbi'], endpoint='ue-contexts-ref-assignEbi'),
    dict(resource=ONEUECONTEXTTRANSFER, urls=['/ue-contexts/<int:ueContextID>/transfer'], endpoint='ue-contexts-ref-transfer'),
    dict(resource=UECONTEXTS, urls=['/ue-contexts'], endpoint='ue-contexts'),
    dict(resource=N1N2MSGSUB, urls=['/ue-contexts/<int:ueContextID>/n1-n2-messages/subscriptions'], endpoint='n1n2message-subscriptions'),
    dict(resource=ONEN1N2MSGSUB, urls=['/ue-contexts/<int:ueContextID>/n1-n2-messages/subscriptions/<int:subscriptionId>'], endpoint='n1n2message-subscriptions-ref'),
    dict(resource=SUBSCRIPTIONS, urls=['/subscriptions'], endpoint='subscriptions'),
    dict(resource=ONESUBSCRIPTION, urls=['/subscriptions/<int:subscriptionId>'], endpoint='subscriptions-ref'),
    dict(resource=NONUEN2MSG, urls=['/non-ue-n2-messages'], endpoint='non-ue-n2-msg'),
    dict(resource=NONUEN2MSGSUB, urls=['/non-ue-n2-messages/subscriptions'], endpoint='non-ue-n2-msg-subscriptions'),
    dict(resource=ONENONUEN2MSGSUB, urls=['/non-ue-n2-messages/subscriptions/<int:n2NotifySubscriptionId>'], endpoint='non-ue-n2-msg-subscriptions-ref'),
]

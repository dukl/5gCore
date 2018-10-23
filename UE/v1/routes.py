from __future__ import absolute_import

from .api.FromAMFInterface import AMFSIDE


routes = [
    dict(resource=AMFSIDE, urls=['/fromamfside'], endpoint='FromAMFInterface'),
]

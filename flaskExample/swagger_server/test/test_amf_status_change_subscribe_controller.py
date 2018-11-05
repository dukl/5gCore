# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestAMFStatusChangeSubscribeController(BaseTestCase):
    """AMFStatusChangeSubscribeController integration test stubs"""

    def test_amf_status_change_subscribe(self):
        """Test case for amf_status_change_subscribe

        Namf_Communication AMF Status Change Subscribe service Operation
        """
        response = self.client.open(
            '/subscriptions',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

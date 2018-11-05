# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestAMFStatusChangeSubscribeModifyController(BaseTestCase):
    """AMFStatusChangeSubscribeModifyController integration test stubs"""

    def test_amf_status_change_subscribe_modfy(self):
        """Test case for amf_status_change_subscribe_modfy

        Namf_Communication AMF Status Change Subscribe Modify service Operation
        """
        response = self.client.open(
            '/subscriptions/{subscriptionId}'.format(subscriptionId='subscriptionId_example'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

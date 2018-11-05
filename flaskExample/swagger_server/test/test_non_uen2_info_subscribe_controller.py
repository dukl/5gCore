# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestNonUEN2InfoSubscribeController(BaseTestCase):
    """NonUEN2InfoSubscribeController integration test stubs"""

    def test_non_ue_n2_info_subscribe(self):
        """Test case for non_ue_n2_info_subscribe

        Namf_Communication Non UE N2 Info Subscribe service Operation
        """
        response = self.client.open(
            '/non-ue-n2-messages/subscriptions',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

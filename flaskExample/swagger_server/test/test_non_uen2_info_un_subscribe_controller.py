# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestNonUEN2InfoUnSubscribeController(BaseTestCase):
    """NonUEN2InfoUnSubscribeController integration test stubs"""

    def test_non_ue_n2_info_un_subscribe(self):
        """Test case for non_ue_n2_info_un_subscribe

        Namf_Communication Non UE N2 Info UnSubscribe service Operation
        """
        response = self.client.open(
            '/non-ue-n2-messages/subscriptions/{n2NotifySubscriptionId}'.format(n2NotifySubscriptionId='n2NotifySubscriptionId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

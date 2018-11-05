# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestNonUEN2MessageTransferController(BaseTestCase):
    """NonUEN2MessageTransferController integration test stubs"""

    def test_non_ue_n2_message_transfer(self):
        """Test case for non_ue_n2_message_transfer

        Namf_Communication Non UE N2 Message Transfer service Operation
        """
        response = self.client.open(
            '/non-ue-n2-messages/transfer',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

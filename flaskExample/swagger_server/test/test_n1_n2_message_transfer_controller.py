# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestN1N2MessageTransferController(BaseTestCase):
    """N1N2MessageTransferController integration test stubs"""

    def test_n1_n2_message_transfer(self):
        """Test case for n1_n2_message_transfer

        Namf_Communication N1N2 Message Transfer (UE Specific) service Operation
        """
        response = self.client.open(
            '/ue-contexts/{ueContextId}/n1-n2-messages'.format(ueContextId='ueContextId_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

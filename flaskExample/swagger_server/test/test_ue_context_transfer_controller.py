# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestUEContextTransferController(BaseTestCase):
    """UEContextTransferController integration test stubs"""

    def test_ue_context_transfer(self):
        """Test case for ue_context_transfer

        Namf_Communication UEContextTransfer service Operation
        """
        response = self.client.open(
            '/ue-contexts/{ueContextId}/transfer'.format(ueContextId='ueContextId_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

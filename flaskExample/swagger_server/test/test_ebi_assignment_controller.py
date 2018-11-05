# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestEBIAssignmentController(BaseTestCase):
    """EBIAssignmentController integration test stubs"""

    def test_ebi_assignment(self):
        """Test case for ebi_assignment

        Namf_Communication EBI Assignment service Operation
        """
        response = self.client.open(
            '/ue-contexts/{ueContextId}/assignEbi'.format(ueContextId='ueContextId_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

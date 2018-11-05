# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestCreateUEContxtController(BaseTestCase):
    """CreateUEContxtController integration test stubs"""

    def test_create_ue_context(self):
        """Test case for create_ue_context

        Namf_Communication CreateUEContext service Operation
        """
        response = self.client.open(
            '/ue-contexts/{ueContextId}'.format(ueContextId='ueContextId_example'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

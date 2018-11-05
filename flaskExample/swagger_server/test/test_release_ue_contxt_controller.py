# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestReleaseUEContxtController(BaseTestCase):
    """ReleaseUEContxtController integration test stubs"""

    def test_release_ue_context(self):
        """Test case for release_ue_context

        Namf_Communication ReleaseUEContext service Operation
        """
        response = self.client.open(
            '/ue-contexts/{ueContextId}/release'.format(ueContextId='ueContextId_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

from unittest import TestCase
import os
import json

import pytero

api_key = os.environ["NATERO_API_KEY"]


class TestClient(TestCase):
    def test_client_constructor(self):
        client = pytero.NateroClient(api_key, region='us')
        self.assertIsNotNone(client)

    def test_invalid_region_constructor(self):
        self.assertRaises(Exception, pytero.NateroClient,
                          api_key, region='invalid')

    def test_get_method(self):
        client = pytero.NateroClient(api_key)
        res = client.get("accounts")
        self.assertEqual(res.status_code, 200, msg=msg)

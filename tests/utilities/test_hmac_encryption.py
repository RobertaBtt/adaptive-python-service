import unittest
import hashlib
import hmac
import base64


class TestHMACEncryption(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.API_SECRET_KEY = "API_SECRET_CLIENT1"
        self.digest_mode = hashlib.sha256

        self.payload = '''
        {
              "event": "SERVER_UPDATE",
              "updates": [
                {
                  "item": "gadgets",
                  "action": "add",
                  "quantity": 20
                },
                {
                  "item": "widgets",
                  "action": "remove",
                  "quantity": 10
                }
              ]
}'''

    def test_hmac_encryption(self):
        # creating a cryptographic hash of the webhook payload
        # This unique signature will be sent in the header

        hmac_result = hmac.new(
            self.API_SECRET_KEY.encode('utf-8'),
            self.payload.encode('utf-8'),
            digestmod=hashlib.sha256)

        hmac_digest = hmac_result.digest()

        computed_mac = base64.b64encode(hmac_digest)
        expected_result = '7wrb5ObQ8Usa1fOYjsK46VmFhtAz+nHtuvU9sP9XClA='.encode('utf-8')
        # print(computed_mac)  # 7wrb5ObQ8Usa1fOYjsK46VmFhtAz+nHtuvU9sP9XClA=
        result = hmac.compare_digest(computed_mac, expected_result)
        self.assertEqual(computed_mac, expected_result)
        self.assertTrue(result)

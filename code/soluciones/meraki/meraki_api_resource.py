"""
Meraki API Resource
"""
import json
import requests

class MerakiAPIResource:
    """ Simplifies the creation of Meraki API resources. """

    url = "https://dashboard.meraki.com/api/v0"

    def __init__(self, key, prefix=None, resource_id=None):
        self.resource_id = resource_id
        self.key = key
        if resource_id is not None:
            self.prefix = prefix + "/" + resource_id
        else:
            self.prefix = prefix

    def _headers_(self):
        return {
            "Content-Type": "application/json",
            "X-Cisco-Meraki-API-Key": self.key
        }

    def _url_(self, endpoint=None):
        if endpoint is None and self.prefix is None:
            endpoint = ""
        elif endpoint is None and self.prefix is not None:
            endpoint = self.prefix
        elif endpoint is not None and self.prefix is not None:
            endpoint = self.prefix + endpoint
        print(self.url + endpoint)
        return self.url + endpoint

    def _get_(self, endpoint=None):
        return requests.get(
            self._url_(endpoint),
            headers=self._headers_()
        )

    def _post_(self, data):
        return requests.post(
            self._url_(),
            headers=self._headers_(),
            data=json.dumps(data)
        )

    def _put_(self, data):
        return requests.put(
            self._url_(),
            headers=self._headers_(),
            data=json.dumps(data)
        )

    def _delete_(self):
        return requests.delete(
            self._url_(),
            headers=self._headers_()
        )

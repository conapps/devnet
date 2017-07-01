"""
Lazy Class
----------
"""

import requests


class LazyRequests():
    """
    Allow to call requests lazily.
    """

    cached = None

    def __init__(self, url, headers, data=None):
        self.url = url
        self.headers = headers
        self.data = data

    def get(self):
        def func():
            return requests.get(self.url, headers=self.headers)
        self.cached = func
        return self

    def post(self):
        def func():
            return requests.post(self.url, headers=self.headers, data=self.data)
        self.cached = func
        return self

    def put(self):
        def func():
            return requests.put(self.url, headers=self.headers, data=self.data)
        self.cached = func
        return self

    def delete(self):
        def func():
            return requests.delete(self.url, headers=self.headers)
        self.cached = func
        return self

    def call(self):
        if self.cached is None:
            raise ValueError("No cached function found.")
        return self.cached()

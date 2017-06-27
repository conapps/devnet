"""
Meraki Devices API Resource
"""

import urllib
from meraki_api_resource import MerakiAPIResource

class Device(MerakiAPIResource):
    """ Meraki API Device resource. """

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def clients(self, query):
        """
        List the clients of a device, up to a maximum of a month ago. The
        usage of each client is returned in kilobytes. If the device is a
        switch, the switchport is returned; otherwise the switchport field
        is null.
        """
        if query is None:
            raise ValueError("You must set the timespan query value.")
        return self._get_("/clients?" + urllib.parse.urlencode(query))

class Devices(MerakiAPIResource):
    """ Meraki API Devices resource. """

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def get(self, serial):
        """ Gets an Meraki Device API resource. """
        return Device(self.key, self.prefix, serial)

    def clients(self, serial, query):
        """ Returns a Device Clients API Resource. """
        return self.get(serial).clients(query)

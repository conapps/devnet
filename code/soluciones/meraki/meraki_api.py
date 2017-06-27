"""
Meraki API helpers
"""

from meraki_api_resource import MerakiAPIResource
from devices import Devices, Device
from organizations import Organizations, Organization
from networks import Networks, Network

class MerakiAPI(MerakiAPIResource):
    """ Meraki API class helper """

    def __init__(self, key):
        if key is None:
            raise ValueError("The 'key' value must be defined.")
        MerakiAPIResource.__init__(self, key)

    def organizations(self, organization_id=None):
        """ Returns an API Organization Resource. """
        if organization_id is None:
            return Organizations(self.key, "/organizations")
        else:
            return Organization(self.key, "/organizations", organization_id)

    def devices(self, serial=None):
        """ Returns an API Devices Resource. """
        if serial is None:
            return Devices(self.key, "/devices")
        else:
            return Device(self.key, "/devices", serial)

    def networks(self, network_id=None):
        """ Returns an API Devices Resource. """
        if network_id is None:
            return Networks(self.key, "/networks")
        else:
            return Network(self.key, "/networks", network_id)

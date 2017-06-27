"""
Meraki Networks API Resource
"""

import urllib
from meraki_api_resource import MerakiAPIResource
from utils import clean

class Network(MerakiAPIResource):
    """ Meraki API Network resource. """

    _parameters_ = ["name", "timeZone", "tags", "type"]

    _traffic_parameters_ = ["timespan", "deviceType"]

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def show(self):
        """ Return a network. """
        return self._get_()

    def create(self, data):
        """ Create a network. """
        return self._post_(clean(data, self._parameters_))

    def update(self, data):
        """ Update a network. """
        return self._put_(clean(data, self._parameters_))

    def delete(self):
        """ Delete a network. """
        return self._delete_()

    def traffic(self, query):
        """
        The traffic analysis data for this network. Traffic Analysis with
        Hostname Visibility must be enabled on the network.
        """
        if query["timespan"] is None:
            raise ValueError("You must set the timespan query value.")
        query = clean(query, self._traffic_parameters_)
        return self._get_("/traffic?" + urllib.parse.urlencode(query))

class Networks(MerakiAPIResource):
    """ Meraki API Networks resource. """

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def index(self):
        """ List the networks in an organization. """
        return self._get_()

    def get(self, network_id=None):
        """ Gets an Meraki Network API resource """
        if network_id is None:
            prefix = self.prefix
        else:
            prefix = self.prefix + "/" + network_id
        return Network(self.key, prefix)

    def show(self, network_id):
        """ Return a network. """
        return self.get(network_id).show()

    def create(self, data):
        """ Create a new dashboard administrator """
        return self.get().create(data)

    def update(self, network_id, data):
        """ Update a network. """
        return self.get(network_id).update(data)

    def delete(self, network_id):
        """ Delete a network. """
        return self.get(network_id).delete()

    def traffic(self, network_id, query):
        """
        The traffic analysis data for this network. Traffic Analysis with
        Hostname Visibility must be enabled on the network.
        """
        return self.get(network_id).traffic(query)

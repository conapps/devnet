"""
Meraki Devices API Resource
"""

from meraki_api_resource import MerakiAPIResource
from utils import clean

class Admin(MerakiAPIResource):
    """ Meraki API Organization Admin resource. """

    _parameters_ = ["email", "name", "orgAccess", "tags", "networks"]

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def create(self, data):
        """ Create a new dashboard administrator """
        return self._post_(clean(data, self._parameters_))

    def update(self, data):
        """ Update an administrator """
        self._put_(clean(data, self._parameters_))

    def delete(self):
        """
        Revoke all access for a dashboard administrator within this
        organization.
        """
        self._delete_()

class Admins(MerakiAPIResource):
    """ Meraki API Organization Admins resource. """

    def __init__(self, key, prefix, resouce_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resouce_id)

    def index(self):
        """ List the dashboard administrators in this organization """
        return self._get_()

    def get(self, admin_id):
        """ Gets a Meraki Organization Admin API resource """
        return Admin(self.key, self.prefix, admin_id)

    def create(self, data):
        """ Create a new dashboard administrator """
        return Admin(self.key, self.prefix).create(data)

    def update(self, admin_id, data):
        """ Update an administrator. """
        return self.get(admin_id).update(data)

    def delete(self, admin_id):
        """
        Revoke all access for a dashboard administrator within this
        organization.
        """
        return self.get(admin_id).delete()

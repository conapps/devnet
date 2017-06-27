"""
Meraki Organizations API Resource
"""

from meraki_api_resource import MerakiAPIResource
from admins import Admins, Admin
from networks import Networks

class Organization(MerakiAPIResource):
    """ Meraki API Organization resource. """

    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def admins(self, admin_id=None):
        """ Returns an Orgaization Admins API Resource. """
        prefix = self.prefix + "/admins"
        if admin_id is None:
            return Admins(self.key, prefix)
        else:
            return Admin(self.key, prefix, admin_id)

    def networks(self):
        """ Returns an Orgaization Networks API Resource. """
        return Networks(self.key, self.prefix + "/networks")

class Organizations(MerakiAPIResource):
    """ Meraki API Organizations resource. """
    def __init__(self, key, prefix, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def get(self, organization_id):
        """ Gets a Meraki Organization API resource """
        return Organization(self.key, self.prefix, organization_id)

    def index(self):
        """ List the organizations that the user has privileges on. """
        return self._get_()

    def admins(self, organization_id, admin_id=None):
        """ Returns an Orgaization Admins resource. """
        return self.get(organization_id).admins(admin_id)

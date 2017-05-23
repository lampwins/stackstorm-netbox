
from lib.action import NetboxBaseAction


class NetboxDCIMGetIPAddresses(NetboxBaseAction):
    """Get IP Addresses"""

    def run(self, **kwargs):
        """Get IP Addresses"""
        endpoint_uri = '/api/ipam/ip-addresses/'
        return self.get(endpoint_uri, **kwargs)

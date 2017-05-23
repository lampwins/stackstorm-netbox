
from lib.action import NetboxBaseAction


class NetboxDCIMGetDevice(NetboxBaseAction):
    """Get device(s)"""

    def run(self, **kwargs):
        """Get device(s)"""
        endpoint_uri = '/api/dcim/devices/'
        return self.get(endpoint_uri, **kwargs)

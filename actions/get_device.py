
from lib.action import NetboxBaseAction


class NetboxGetDevice(NetboxBaseAction):
    """Get a device by serial number"""

    def run(self, **kwargs):
        """Get a device by serial number"""
        endpoint_uri = '/api/dcim/devices/'
        return self.get(endpoint_uri, kwargs)

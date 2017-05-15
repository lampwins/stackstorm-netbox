
from lib.action import NetboxBaseAction


class NetboxGetDevice(NetboxBaseAction):
    """Get a device by serial number"""

    def run(self, serial):
        """Get a device by serial number"""
        endpoint_uri = '/api/dcim/devices/?serial=' + serial
        return self.get(endpoint_uri)

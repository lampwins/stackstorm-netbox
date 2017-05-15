
from lib.action import NetboxBaseAction


class NetboxGetInterfaces(NetboxBaseAction):
    """Get device interfaces"""

    def run(self, device_id):
        """Get the interfaces for a device by its ID"""
        endpoint_uri = '/api/dcim/interfaces/?device_id=' + device_id
        return self.get(endpoint_uri)

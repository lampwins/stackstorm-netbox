
from lib.action import NetboxBaseAction


class NetboxGetInterfaces(NetboxBaseAction):
    """Get device interfaces"""

    def run(self, **kwargs):
        """Get the interfaces for a device by its ID"""
        endpoint_uri = '/api/dcim/interfaces/
        return self.get(endpoint_uri, kwargs)

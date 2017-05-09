
from st2actions.runners.pythonrunner import Action

import requests

__all__ = [
    'NetboxBaseAction'
]


class NetboxBaseAction(Action):
    """Base Action for all Netbox API based actions
    """

    def __init__(self, config):
        super(NetboxBaseAction, self).__init__(config)

    def get(self, endpoint_uri):
        """Make a get request to the API URI passed in
        """
        
        if self.config['use_ssl']:
            url = 'https://'
        else:
            url = 'http://'

        url = url + self.config['hostname'] + endpoint_uri

        headers = {
            'Authorization': 'Token ' + self.config['api_token'],
            'Accept': 'application/json'
        }

        r = requests.get(url, verify=self.config['ssl_verify'])

        return {'raw': r.json()}

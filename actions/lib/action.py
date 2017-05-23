
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

    def get(self, endpoint_uri, **kwargs):
        """Make a get request to the API URI passed in
        """

        self.logger.info("Calling base get with kwargs: {}".format(kwargs))

        if self.config['use_https']:
            url = 'https://'
        else:
            url = 'http://'

        url = url + self.config['hostname'] + endpoint_uri

        headers = {
            'Authorization': 'Token ' + self.config['api_token'],
            'Accept': 'application/json'
        }

        # transform `in__id` if present
        if kwargs.get('in__id'):
            kwargs['in__id'] = ','.join(kwargs['in__id'])

        r = requests.get(url, verify=self.config['ssl_verify'], headers=headers, params=kwargs)

        return {'raw': r.json()}

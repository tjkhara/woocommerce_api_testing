
from ssqaapitest.src.configs.hosts_config import API_HOSTS
from ssqaapitest.src.utilities.credentials_helper import CredentialsUtility
import requests
import os
from requests_oauthlib import OAuth1

class RequestsUtility(object):

    def __init__(self):
        api_keys = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(api_keys.get('wc_key'), api_keys.get('wc_secret'))
        self.status_code = None

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        url = self.base_url + endpoint

        response = requests.post(url=url, data=payload, headers=headers, auth=self.auth)
        self.status_code = response.status_code
        assert self.status_code == int(expected_status_code), f'Expected status code {expected_status_code} ' \
                                                              f'but actual {self.status_code}'
        return response.json()

    def get(self):
        pass
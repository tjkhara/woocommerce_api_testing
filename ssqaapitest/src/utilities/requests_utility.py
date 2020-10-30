
from ssqaapitest.src.configs.hosts_config import API_HOSTS
from ssqaapitest.src.utilities.credentials_utility import CredentialsUtility
import requests
import os
from requests_oauthlib import OAuth1
import logging as logger

class RequestsUtility(object):

    def __init__(self):
        api_keys = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(api_keys.get('wc_key'), api_keys.get('wc_secret'))
        self.status_code = None
        self.expected_status_code = None
        self.url = None
        self.response = None
        self.response_json = None

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code." \
                                                              f"Expected {self.expected_status_code}" \
                                                              f"Actual {self.status_code}" \
                                                              f"url: {self.url}" \
                                                              f"Response json: {self.response_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        # This is the actual request
        self.response = requests.post(url=self.url, data=payload, headers=headers, auth=self.auth)
        self.status_code = self.response.status_code
        self.expected_status_code = expected_status_code
        self.response_json = self.response.json()
        self.assert_status_code() # This checks the status code is as expected

        logger.debug(f"POST API response: {self.response_json}")

        return self.response_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        self.response = requests.get(url=self.url, data=payload, headers=headers, auth=self.auth)
        self.status_code = self.response.status_code
        # We check the expected status code here
        self.expected_status_code = expected_status_code
        self.response_json = self.response.json()
        self.assert_status_code()

        logger.debug(f"GET API response: {self.response_json}")

        return self.response_json




from ssqaapitest.src.utilities.generic_utility import generate_random_email_and_password
from ssqaapitest.src.utilities.requests_utility import RequestsUtility
import logging as logger
import json

class CustomerHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            ep = generate_random_email_and_password()
            email = ep.get('email')
        if not password:
            password = 'password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)


        create_user_json = self.requests_utility.post('customers', payload=json.dumps(payload), expected_status_code=201)

        logger.debug(f"API response: {create_user_json}")

        return create_user_json

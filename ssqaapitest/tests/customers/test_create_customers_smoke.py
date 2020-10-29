import json

import pytest
import logging as logger
from ssqaapitest.src.utilities.generic_utility import generate_random_email_and_password
from ssqaapitest.src.utilities.helpers.customers_helper import CustomerHelper
from ssqaapitest.src.dao.customers_dao import CustomersDAO
from ssqaapitest.src.utilities.requests_utility import RequestsUtility
import random

@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only.")

    rand_info = generate_random_email_and_password()
    logger.info(rand_info)

    email = rand_info.get("email")
    password = rand_info.get("password")

    # make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify status code of the call

    # verify email and first name in the response
    assert cust_api_info['email'] == email, f"Create customer api returned wrong email. Email {email}"
    assert cust_api_info['first_name'] == '', f"Create customer API returned a value for the first name" \
                                              f"but it should be empty."

    # verify customer is created in the database
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)
    # import pdb; pdb.set_trace()

    assert cust_api_info['id'] == cust_info[0]['ID'], f"API id received {cust_api_info['id']} and" \
                                                      f" id in database {cust_info['ID']}" \
                                                      f" do not match."

@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():

    # Get a customer from the database
    cust_dao = CustomersDAO()
    existing_customer = cust_dao.get_random_customer_from_db()
    existing_customer_email = existing_customer[0]['user_email']

    # Create a customer by calling the api
    requests_helper = RequestsUtility()
    payload = {'email': existing_customer_email, 'password': 'password'}
    response = requests_helper.post(endpoint='customers', payload=json.dumps(payload), expected_status_code=400)
    # import pdb;
    # pdb.set_trace()
    assert response['data']['status'] == 400, f"The error code for existing customer email is not 400"
    assert response['code'] == 'registration-error-email-exists', f"Create customer with existing user" \
                                                                  f"error code is not as expected." \
                                                                  f"Expected: registration-error-email-exists" \
                                                                  f"Received: {response['code']}"


import pytest
import logging as logger
from ssqaapitest.src.utilities.generic_utilities import generate_random_email_and_password
from ssqaapitest.src.utilities.helpers.customers_helper import CustomerHelper

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

    return True

    # verify status code of the call

    # verify email in the response

    # verify customer is created in the database
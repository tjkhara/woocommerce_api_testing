import pytest
import logging as logger
from ssqaapitest.src.utilities.generic_utilities import generate_random_email_and_password

@pytest.mark.tcid29
def test_create_customer_only_email_password():

    logger.info("TEST: Create new customer with email and password only.")

    rand_info = generate_random_email_and_password()
    logger.info(rand_info)

    email = rand_info.get("email")
    password = rand_info.get("password")

    # create payload
    payload = {"email":email, "password":password}

    # make the call


    # verify status code of the call

    # verify email in the response

    # verify customer is created in the database
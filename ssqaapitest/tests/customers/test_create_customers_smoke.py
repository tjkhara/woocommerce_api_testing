import pytest
import logging as logger
from ssqaapitest.src.utilities.generic_utility import generate_random_email_and_password
from ssqaapitest.src.utilities.helpers.customers_helper import CustomerHelper
from ssqaapitest.src.dao.customers_dao import CustomersDAO


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

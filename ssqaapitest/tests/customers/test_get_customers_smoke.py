import pytest
from ssqaapitest.src.utilities.requests_utility import RequestsUtility
import logging as logger

@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    request_helper = RequestsUtility()
    response_api = request_helper.get('customers')
    assert response_api, f"Response of list all customers is empty."

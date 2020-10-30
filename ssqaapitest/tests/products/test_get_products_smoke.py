import pytest
from ssqaapitest.src.utilities.requests_utility import RequestsUtility


@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():
    request_helper = RequestsUtility()
    response_api = request_helper.get('products')
    import pdb; pdb.set_trace()
    assert response_api, f"Response of list all products is empty."

from ssqaapitest.src.utilities.generic_utility import generate_random_string
from ssqaapitest.src.utilities.helpers.products_helper import ProductHelper
from ssqaapitest.src.dao.products_dao import ProductsDAO
import json
import pytest

@pytest.mark.products
@pytest.mark.tcid26
def test_create_1_simple_product():

    # generate data for the product
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    # make the call
    product_helper_obj = ProductHelper()
    product_response = product_helper_obj.call_create_product(json.dumps(payload))


    # verify response is not empty
    assert product_response, f"Create product API response is empty. Payload is {payload}"
    assert product_response['name'] == payload['name'], f"Create product API response has unexpected name" \
                                                        f"Expected is {payload['name']}" \
                                                        f"Actual is {product_response['name']}"


    # verify the product exists in db
    products_dao_obj = ProductsDAO()
    sql_response = products_dao_obj.get_product_by_id(product_response['id'])

    # match the information in the db with the information in the api call
    assert payload['name'] == sql_response[0]['post_title'], f"Product name from payload is different from database response" \
                                                          f"Payload name is {payload['name']}" \
                                                          f"In response from db is {sql_response['name']}"

    import pdb; pdb.set_trace()
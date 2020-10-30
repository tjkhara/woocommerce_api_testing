import pytest
from ssqaapitest.src.utilities.requests_utility import RequestsUtility
from ssqaapitest.src.dao.products_dao import ProductsDAO
from ssqaapitest.src.utilities.helpers.products_helper import ProductHelper


@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():
    request_helper = RequestsUtility()
    response_api = request_helper.get('products')
    # import pdb; pdb.set_trace()
    assert response_api, f"Response of list all products is empty."

@pytest.mark.products
@pytest.mark.tcid25
def test_get_products_by_id():

    # Get an existing product from db
    products_dao_obj = ProductsDAO()
    random_product = products_dao_obj.get_random_product_from_db()
    random_product_name = random_product[0]['post_name']
    random_product_id = random_product[0]['ID']

    # Make the call from the api
    # Get the product with this id
    prod_helper_obj = ProductHelper()
    response_product = prod_helper_obj.get_product_by_id(random_product_id)
    response_product_sku = response_product['sku']
    response_product_name = response_product['name']

    # Verify the response
    assert random_product_name.lower() == response_product_name.lower(), f"Get product from db does not match product" \
                                                                         f"from api using id." \
                                                                         f"Product from db:" \
                                                                         f"{random_product_name}" \
                                                                         f"Product from API:" \
                                                                         f"{response_product_name}"
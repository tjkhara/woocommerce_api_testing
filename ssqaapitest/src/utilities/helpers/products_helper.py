from ssqaapitest.src.utilities.requests_utility import RequestsUtility


class ProductHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_product_by_id(self, product_id):
        return self.requests_utility.get(f"products/{product_id}")
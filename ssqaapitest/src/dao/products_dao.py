import random

from ssqaapitest.src.utilities.db_utility import DBUtility

class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_product_by_id(self, id):
        pass
        # Need to implement this later

    def get_random_product_from_db(self, qty=1):
        sql = f"SELECT * FROM wordpress.wp_posts WHERE post_type = 'product' LIMIT 5000;"
        response_sql = self.db_helper.execute_select(sql=sql)
        return random.sample(response_sql, int(qty))
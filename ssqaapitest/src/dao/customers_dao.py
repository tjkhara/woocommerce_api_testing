from ssqaapitest.src.utilities.db_utility import DBUtility
import random


class CustomersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM `wordpress`.`wp_users` WHERE user_email = '{email}';"
        response_sql = self.db_helper.execute_select(sql=sql)
        return response_sql
        # import pdb; pdb.set_trace()

    def get_first_customer(self):
        sql = f"SELECT * FROM `wordpress`.`wp_users` LIMIT 1;"
        response_sql = self.db_helper.execute_select(sql=sql)
        return response_sql

    def get_random_customer_from_db(self, quantity=1):
        sql = f"SELECT * FROM `wordpress`.`wp_users` ORDER BY id DESC LIMIT 5000;"
        response_sql = self.db_helper.execute_select(sql=sql)
        return random.sample(response_sql, int(quantity))
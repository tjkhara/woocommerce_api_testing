from ssqaapitest.src.utilities.db_utility import DBUtility



class CustomersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM `wordpress`.`wp_users` WHERE user_email = '{email}';"
        response_sql = self.db_helper.execute_select(sql=sql)
        return response_sql
        # import pdb; pdb.set_trace()
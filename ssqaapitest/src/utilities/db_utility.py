import logging as logger

import pymysql
from ssqaapitest.src.utilities.credentials_utility import CredentialsUtility


class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()
        self.host = "localhost"
        self.port = 33002
        self.socket = None


    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.creds['db_user'],
                                     password=self.creds['db_password'], port=self.port)
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()
        try:
            logger.debug(f"Executing: {sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            response_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error is {str(e)}")
        finally:
            conn.close()

        return response_dict


    def execute_sql(self, sql):
        pass
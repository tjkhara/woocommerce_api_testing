import os

class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():

        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')
        if not (wc_key and wc_secret):
            raise Exception("The API credentials wc_key or wc_secret are not set")
        else:
            return {
                'wc_key':wc_key,
                'wc_secret':wc_secret
            }

    @staticmethod
    def get_db_credentials():
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        if not (db_user and db_password):
            raise Exception("The database credentials db_user or db_password are not set")
        else:
            return {
                'db_user': db_user,
                'db_password': db_password
            }
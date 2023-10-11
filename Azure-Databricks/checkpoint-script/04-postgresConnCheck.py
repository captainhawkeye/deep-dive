import psycopg2
import requests
import json
from datetime import datetime
try:
    logger.log_message('INFO', "[Started] - Postgres Connection Started")
    AUTH_TENANT_ID = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key='AUTH-TENANT-ID')
    AUTH_GRANT_TYPE = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key='AUTH-GRANT-TYPE')
    AUTH_CLIENT_ID = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key='ADB-POSTGRES-SP-CLIENTID')
    AUTH_CLIENT_SECRET = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key='ADB-POSTGRES-SP-SECRET')
    AUTH_RESOURCE = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key='AUTH-RESOURCE')
    USER_SP = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key='USER-SP')

    access_token = 'NA'
    AUTH_TOKEN_URL = f"https://login.microsoftonline.com/"+AUTH_TENANT_ID+"/oauth2/token"
    AUTH_PAYLOAD = {'grant_type':AUTH_GRANT_TYPE, 'client_id':AUTH_CLIENT_ID, 'client_secret':AUTH_CLIENT_SECRET, 'resource':AUTH_RESOURCE}
    AUTH_HEADER = {'Content-Type':'application/x-www-form-urlencoded'}
    response = requests.post(url=AUTH_TOKEN_URL, data=AUTH_PAYLOAD, headers=AUTH_HEADER)
    print(response.status_code)

    if response.status_code == 200:
        token_details = json.loads(response.text)
        access_token = token_details['access_token']
    USER = USER_SP
    PASSWORD = access_token
    postgres_cred_exp_ts = datetime.utcfromtimestamp(int(token_details['expires_on'])-60)
    print(access_token)

    SSLMODE = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key='SSLMODE-PG')
    HOST_NAME = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key='HOST-NAME-PG')
    PORT = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key='PORT-PG')
    DATABASE = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key='DATABASE-PG')
    postgres_conn = psycopg2.connect(host=HOST_NAME, database=DATABASE, user=USER_SP, password=PASSWORD, sslmode=SSLMODE)
    logger.log_message('INFO', "[Completed] - Postgres Connection Completed")
    status_dict['postgres_connection'] = 'SUCCESS'
except:
    logger.log_message('INFO', "[Failed] - Postgres Connection Failed")
    status_dict['postgres_connection'] = 'FAILED'
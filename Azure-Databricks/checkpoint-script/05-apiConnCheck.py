import requests
import json
app_host = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key="BATCH-APP-HOST")
app_port = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key="BATCH-APP-PORT")
try:
    logger.log_message('INFO', "[Started] - API Connection Started")
    job_names_values = {
        'autorun_cash' : dbutils.secrets.get(scope=AKV_SCOPE_NAME, key="AUTORUN-CASH-LIVE"),
        'sku_group_sku_refresh' : dbutils.secrets.get(scope=AKV_SCOPE_NAME, key="SKU-GRP-REFRESH-LIVE"),
        'sku_group_sku_count_refresh' : dbutils.secrets.get(scope=AKV_SCOPE_NAME, key="SKU-GRP-COUNT-LIVE"),
        'results' : '/optumera/pharmacy/recommresultservice/api/protected/internal/isLive',
        'master_fetch' : '/optumera/pharmacy/recomfetchmasterservice/api/protected/internal/isLive',
    }
    for job_name in job_names_values:
        job_url = f'https://{app_host}:{app_port}{job_names_values[job_name]}'
        x = requests.get(job_url, verify=False)
        if x.status_code == 200:
            print(json.loads(x.text))
            logger.log_message('INFO', job_name.upper() + " is up, with status code : " + str(x.status_code))
            status_dict['api '+str(job_name)] = 'UP with status code'+str(x.status_code)
        else:
            logger.log_message('INFO', job_name.upper() + " is down, with status code : " + str(x.status_code))
            status_dict['api '+str(job_name)] = 'DOWN with status code'+str(x.status_code)
    logger.log_message('INFO', "[Completed] - API Connection Completed")
except Exception as e:
    logger.log_message('INFO', "[Failed] - API Connection Failed")
    status_dict['api'] = 'FAILED'
try:
    logger.log_message('INFO', "[Started] - Configuration")
    protocol, container, storage_account, storage_type, akv_storage_type = 'abfss', P_BLOBSTORAGE, P_STORAGEACCOUNT, 'dfs', 'blob'
    client_id = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key=f"ADB-{akv_storage_type}-SP-CLIENTID")
    tenant_id = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key="SP-TENANT-ID")
    client_secret = dbutils.secrets.get(scope=AKV_SCOPE_NAME, key=f"ADB-{akv_storage_type}-SP-SECRET")
    spark.conf.set(f"fs.azure.account.auth.type.{storage_account}.dfs.core.windows.net", "OAuth")
    spark.conf.set(f"fs.azure.account.oauth.provider.type.{storage_account}.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
    spark.conf.set(f"fs.azure.account.oauth2.client.id.{storage_account}.dfs.core.windows.net", client_id)
    spark.conf.set(f"fs.azure.account.oauth2.client.secret.{storage_account}.dfs.core.windows.net", client_secret)
    spark.conf.set(f"fs.azure.account.oauth2.client.endpoint.{storage_account}.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")
    logger.log_message('INFO', "[Completed] - Configurations")

    logger.log_message('INFO', "[Started] - Blob Connection")
    a = dbutilts.fs.ls(protocol + '://' + container +'@' + storage_account + '.' + storage_type + '.core.windows.net')
    logger.log_message('INFO', "[Completed] - Connection is available")
    status_dict['blob_connection'] = 'SUCCESS'
except Exception as e:
    logger.log_message('INFO', "[Failed] - Connection Failed")
    status_dict['blob_connection'] = 'FAILED'
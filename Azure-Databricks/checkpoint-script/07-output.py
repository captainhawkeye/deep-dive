def create_result_file(df, datetime, dbutils, P_TARGETSOURCE, BLOB_HEADER, COLUMN_DELIMITER, new_file, protocol, storage_type, P_BLOBSTORAGE, P_STORAGEACCOUNT, P_ROOT_FILE_PATH):
    df.coalesce(1).write.format("com.databricks.spark.csv").option("header", BLOB_HEADER).option("delimiter", COLUMN_DELIMITER).option("emptyValue", "").mode("overwrite").save(protocol + "://" + P_BLOBSTORAGE + "@" + P_STORAGEACCOUNT + "." + storage_type + ".core.windows.net" + P_ROOT_FILE_PATH + "/" + P_TARGETSOURCE + "/" + new_file)
    l_output_file = [x for x in __files if x.name.startswith("part-")]
    l_output_file_path = protocol + "://" + P_BLOBSTORAGE + "@" + P_STORAGEACCOUNT + "." + storage_type + ".core.windows.net" + P_ROOT_FILE_PATH + "/" + P_TARGETSOURCE + '/' + "results.csv"
    print(l_output_file_path)
    aa = dbutils.fs.mv(l_output_file[0].path, l_output_file_path)
df = spark.createDataFrame(status_dict.items())
if P_ROOT_FILE_PATH in ["", "/"]:
    P_ROOT_FILE_PATH = ""
P_TARGETSOURCE, BLOB_HEADER, COLUMN_DELIMITER, new_file, protocol, storage_type = 'one_time_check_point', "True", ",", "new_data", 'abfss', 'dfs'
create_result_file(df, datetime, dbutils, P_TARGETSOURCE, BLOB_HEADER, COLUMN_DELIMITER, new_file, protocol, storage_type, P_BLOBSTORAGE, P_STORAGEACCOUNT, P_ROOT_FILE_PATH)
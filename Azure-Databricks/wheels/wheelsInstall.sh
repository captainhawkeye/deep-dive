clustername=$1
dbfs_folder_path=$2
clusterid=$(databricks clusters get --cluster-name $clustername | jq -r .default_tags.ClusterId)

wheel_packages=$(dbfs ls "$dbfs_folder_path")

for package_name in $wheel_packages; do
    databricks libraries install --cluster-id $clusterid --whl $dbfs_folder_path/$package_name
done
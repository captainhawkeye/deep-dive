echo "----------"
echo "Create a Directory to Store Latest Version of Wheels"
echo "----------"

mkdir latestVersion

echo "----------"
echo "Get the Latest Versions of all the Wheels and Copy it into Separate Folder"

ls abc_package*.whl | sed -Ee 's/^(.*-)([0-9.]+)(\.whl)$/\2.-1 \1\2\3/' | sort -t. -n -k1,1 -k2,2 -k3,3 -k4,4 | cut -d\  -f2- | sort -V | tail -n 1 | xargs -i cp {} latestVersion/
sleep 10

echo "----------"
echo "Create Directory on ADB DBFS"
echo "----------"

dbfs mkdirs dbfs:/wheels
sleep 10

echo "----------"
echo "Upload the Latest Wheels on DBFS"
echo "----------"

for file in /latestVersion/*.whl; do
    dbfs cp --overwrite $file dbfs:/wheels/
done
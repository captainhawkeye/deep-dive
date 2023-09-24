**Troubleshooting - phoenix-sqlline not working**

1. Scan meta
`echo "scan 'hbase:meta'" | hbase shell > meta.out`

2. Extract the server names from "meta.out" file
`grep "info:sn" meta.out | awk '{print $4}' | sort | uniq`

3. Create the empty WAL Dirs
`hdfs dfs -mkdir hdfs://mycluster/hbasewal/WALs/<server-name-extracted-above>`

4. Restart the Active HMaster. Important - Online Active HMaster needs to be restarted (From Ambari UI)

5. Some dead region servers will be shown. They should go away after some time.
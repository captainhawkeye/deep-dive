dbutils.fs.put("/databricks/scripts/addhosts.sh", """
#!/bin/bash
sudo echo x.x.x.x abc.com >> /etc/hosts
""", True)
display(dbutils.fs.ls("dbfs:/databricks/scripts/addhosts.sh"))
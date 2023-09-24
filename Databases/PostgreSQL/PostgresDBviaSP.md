Have a Service Principal ready. Make sure Role has been created for mentioned SP in PostgreSQL Server.

Command1:
    curl -X GET -H 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=client_credentials&client_id=<SPClientID>&resource=https://ossrdbms-aad.database.windows.net&client_secret=<SPClientSecret>' https://login.microsoftonline.com/<SPTenantID>/oauth2/token

You'll get a Token after executing above command. Copy the Token.

Command2:
    export PGPASSWORD="<PasteAboveCopiedToken>"

Command3:
    psql "host=<PostgreSQLFullHostName> user=<SPName@PostgreSQLServerNameOnly> dbname=<DBName> sslmode=require"

Now you are logged in to PostgreSQL Server using Service Principal.

Some commands you can try afterwards in Cloudshell:
    select distinct grantor,grantee from information_schema.role_table_grants rtg;      --->        To see schema owner details

    \dt master.*        --->        To see the table owners

    \c <AnotherDBName>      --->        To Move to another DB

    \l      --->        To list down the all the DBs 

Some useful commands to try in Data Studio:
    select * from pg_roles;     --->        To see all the roles in PostgreSQL

    select d.datname as "Name",pg_catalog.pg_get_userbyid(d.datdba) as "Owner" from pg_catalog.pg_database d where d.datname = '<DBName>'order by 1;     --->        To check owner of database

    select pid, datname from pg_catalog.pg_Stat_activity where datname='<DBName>';      --->        To check how many sessions are there in the database

    select pg_terminate_backend(pid) from pg_catalog.pg_Stat_activity where datname='<DBName>';     --->        To kill all active sessions of a database

    drop database <DBName>;     --->        To delete a database


Some other commands:
    pg_dump -Fc -v --host=<PostgreSQLFullHostName> --username=<PostgreSQLAdminUserName@PostgreSQLServerNameOnly> --dbname=<DBName> -f <DumpName>.dump       --->        To take Dump/Backup of a particular DB

    pg_restore -v --no-owner --no-acl --role="SPName" --host=<PostgreSQLFullHostName> --port=5432 --username=<PostgreSQLAdminUserName@PostgreSQLServerNameOnly> --dbname=<NewDBName> <DumpName>.dump        --->        To restore in a particular DB via User Login 

    pg_restore -v --no-owner --no-acl --role="SPName" --host=<PostgreSQLFullHostName> --port=5432 --username=<SPName@PostgreSQLServerNameOnly> --dbname=<NewDBName> <DumpName>.dump     --->        To restore in a particular DB via SP Login
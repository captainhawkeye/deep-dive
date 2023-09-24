**PostgreSQL Single Server - Azure**

Create PG Role for a Service Principal/AAD Group with DB owner privileges:
`SET aad_validate_oids_in_tenant = off;`
`CREATE ROLE "<SP-name>" WITH LOGIN NOSUPERUSER INHERIT CREATEDB NOREPLICATION PASSWORD '<SP-client-ID>' IN ROLE azure_ad_user;`

Create PG Role for a Servie Principal/AAD Group without any privileges (Reader role):
`SET aad_validate_oids_in_tenant = off;`
`CREATE ROLE "<SP-name/AD group>" WITH LOGIN IN ROLE azure_ad_user;`
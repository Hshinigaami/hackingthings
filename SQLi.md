# SQLi
- Leads to unauthorized access to database.
- Can be escalated to RCE,DOS.
- Successful SQLi can lead to persistent backdoor in organization.

## Examples
1. Retrieving hidden data: Get extra information from current database.
2. Union Attacks: Get information from other database.
3. Examining Database: Get current version of database.
4. Subverting Application Logic: 
5. Blind SQLI: 


# SQL Tutorial
-- SQL is not case sensitive for commands, but case sensitive when creating database names
CREATE DATABASE testDB;

-- How to check current Database name
SELECT DB_NAME(); -- This is query
db_name() -- This is in terminal ...  Not tried yet.

-- .bak extension tells the backup db name extension
BACKUP DATABASE testDB
to DISK = 'D:/';

-- Incase of Differential Backup
BACKUP DATABASE testDB
to DISK = 'D:/'
with DIFFERENTIAL;
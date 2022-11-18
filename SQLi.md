# SQLi
- Leads to unauthorized access to database.
- Can be escalated to RCE,DOS.
- Successful SQLi can lead to persistent backdoor in organization.

# Methods
1. Retrieving hidden data: Get extra information from current database.
2. Union Attacks: Get information from other database.
3. Examining Database: Get current version of database.
4. Subverting Application Logic: 

# Types of SQL Injection

1. In-BOund SQL Injection
	a. Data is reflected in the same page, when we enter any values in parameter.
	b. For eg: In username parameter if we enter any injection, it would be reflected somewhere in the page where username is reflected.

2. Error based SQL Injection
	a. If there is no reflection of any parameter values on page, lets go for error based sql injection.
	b. If we inject any query into parameters, page will throw us an error.

3. Union Based SQL Injection\
	a. This injection method, will utilize UNION command which combines one table with another, any prints the output.
	b. How can we detect Union Based SQL Injection
		1. Using ORDER BY clause. If we have a where clause like where ID = 2 or something like that we can use ORDERY BY clause there.
			a. ' ORDER BY 1 ' ORDER BY 2 'ORDER BY 3
			b. Try to order by different columns and check if you recieve any error, we can specify index name ... so no need to specify column name.
		2. Using UNION Clause with NULL Values.
			a. ' UNION SELECT NULL; 'UNION SELECT NULL,NULL; ' UNION SELECT NULL,NULL,NULL;
			b. When number of nulls matches number of columns it might throw us additional row or null point exception error.

4. Blind SQL Injection
	a. When we don't recieve any output or just some minor tweaks are there in response.
	b. Authentication bypass
		1. Most common Blind sql injection because we don't want to see usernames or passwords.
		2. We just want to pass login forms
		3. Common SQL Injection - ' OR 1=1 --; '--
	c. Boolean based: In this, output would be binary. So if username is not available returns false then try UNION statement which is like OR, if admin123 username returns false, then union that with available columns, at one point it will return true, which means false OR true => true . After finding columns try to manipulate to return databases, columns and tables.
	d. Time Based: In this there is no binary output nor we can verify if our statement is working, so this time we use sleep(x) function or similar, which will delay the response. For eg: admin' UNION select 1,sleep(5);-- If this returns response after a 5second delay that means its working, after this follow similar steps like boolean based, since now we know there are total two columns.

# Detecting SQL Injection

1. Lets start with Error based SQL Injection by inserting few characters.
	a. '
	b. "
	c. `(Tilda Character)`

# Process during In-Bound SQL Injection with blog parameter vulnerable to sql injection

- select * from article where id = 0 UNION select 1,2,group_concat(table_name) from INFORMATION_SCHEMA.tables where table_schema='sqli_one'
- select * from article where id = 0 UNION select 1,2,group_concat(column_name) from INFORMATION_SCHEMA.columns where column_name='staff_users'
- select * from article where id = 0 UNION select 1,2,group_concat(usernames, ':', password SEPARATOR '<br>') from staff_users


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

## SQL Statements
select * from users where username == 'admin';
select * from users where username like '%n';
	- This ensures usernames which ends with n
	- like can have % at start,end or in middle. like %n returns admin,john,etc. like a% returns admin,adi,etc. like %mi% returns admin,amiy,etc.
select age,customer from users UNION select day,products from shop;
	- UNION will only work if we have same number of columns on both tables.
insert into tablename (username,password) values (admin,123);
update users set username='root',password='123' where username='admin';
delete from users where username='admin';
	- delete from users; will delete all rows from users table.

# SOLutions
martin => pa$$word
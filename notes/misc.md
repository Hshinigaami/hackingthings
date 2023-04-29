# Index

- [Reverse Proxy](#Reverse-Proxy)
- [Defensive Security](#Defensive-Security)
- [Principles of Security](#Principles-of-Security)
- [SSL Cert](#SSL-Cert)
- [SNI](#SNI)

# Questions
    - What is multiple layer of reverse proxy and how can we attack them.

# Reverse Proxy
    - This means, when client sends a request, a proxy server is sitting in middle of client and server.
    - Then server will send this request to backend servers get the information and then again send back to client.
    - Difference between reverse and normal is, forward proxy server will route the traffic to other clients and not fetch any thing from backend servers.
    - One of the main thing is, reverse proxy won't reveal origin server IP.
    - How? Forward will sit between client and internet, so internet is able to access origin server, so IP Address is reveal.
    - Whereas, reverse proxy sits between internet and Origin IP, thus internet won't be accessing Origin IP whereas they would be accessing reverse proxy(CDN)
    - In this way, Websites are protected from various attacks, as they would be performing it on CDN. And reduces cost as reverse proxy would encrypt and decrypt(SSL and TLS) instead of all origin IP Server AND It also helps is load balancing.

# Defensive Security
## Areas of Defensive Security

## SOC(Security Operation Center)
	a. Detect vulnerabilities if present and not the job to fix them, but they can do.
	b. Intrusion(Network)
	c. Update and patch
	d. Unauthorized Activity (Like attacker logging in from victim account)
	e. Policy violation

	### Threat Intelligence
		a. Gather all information about company to know things in bigger scale.
		b. To know there tactics, techniques and procedures they do when attacks.

## Digital Forensics and Incident Response
	a. Investigation of cyber crimes and gathering facts.
	b. Key areas where  they would focus is analyzing file systems, logs(network, system).
	c. Analyzing system memory whether any malware application is running.

	### Incident Response Team
		a. The aim is to recover damage from attacker in shortest possible time.
		b. If an incident comes, its there duty to analyze and provide a severity level.
		c. If incident is affecting a system, first of all detach that system from others, as to prevent it from spreading. Then recover that system from malware.
		d. After a system is recovered, we need to make a report so as to prevent such attacks in future.

	### Malware Analysis
		a. This is part of Forensics as well, as we would be investigating any malware that is affected our system.
		b. There are two types of malware analysis
			1. Static Analysis: This would require knowledge of Assembly, as we would be investigating the programs, or files which are affected.
			2. Dynamic Analysis: This is where we would run the program in sandbox environment and analyze what the program is doing and make a report on it.

## Copied Notes
- There are many open-source databases out there, like AbuseIPDB, and Cisco Talos Intelligence, where you can perform a reputation and location check for the IP address.

# Principles of Security

# SSL Cert
	1. SSL Cert verifies a websites identity. Now-a-days Every website is issued with a SSL Certificate by hosting providers.
	2. This SSL Cert ensures that any transaction between two systems is secured and encrypted.
	3. How SSL Cert works?
		a. First User tries to connect to website(webserver)
		b. Web server sends the SSL Certificate to browser
		c. They verifies if its correct SSL, then user sends ok I would like to connect.
		d. Webserver sends acknowledge with a digital signed signature to user.
		e. And thus a encrypted channel/session begin between user and webserver.
	4. 
	## Resources:
		1. http://www.steves-internet-guide.com/ssl-certificates-explained/
		2. 

# SNI
	1. SNI means server name indication, when we perform TLS Handshake, at this layer SNI is also validated.
	2. Now why we needed SNI?
		a. Now a days multiple websites with same IP Address is hosted on a web server.
		b. so when we visit a website, before http protocol(which specifies the hostname we want to connect), SSL/TLS handshake is performed i.e SSL cert is given by server to browser.
		c. Since, there are multiple websites with there own ssl cert, server don't know which ssl cert to issue to client.
		d. This is where SNI came(Server Name Indication)
	3. SNI is an extension to TLS protocol, they make it possible to specify domain name, during TLS handshake instead of during HTTP connection which is opened after TLS Handshake.
	4. 
	
# What is Routing?
    - Routing specifies how data packets are transferred in a packet-networks of internet. These internet routing decisions are made by routers.
    - So for ex: if one data packet needs to reach it's destination it can go through one route or some other route with faster reach.
    - Main routing protocols include IP, BGP, OSPF, RIP.
    - Internet protocol is specified with Source, Destination and Data header. Routers identify Destination and sends the packet accordingly.
    - BGP(Border Gateway protocol) tells the router which AS(Autonomous System) to connect inorder to transfer data packets at a faster rate.
        - BGP has it's own AS Database called routing table, that's how this protocol decides where to send the packet.
        - Without BGP, IP protocol would be just hopping from one point to another until it reaches destination.
    - OSPF is Open shortest path first and RIP is Routing Information Protocol which finds the shortest path based upon number of hops.
    
# What is ASN?
    - ASN is Autonomous system numbers, Our internet is made up of networks, and each bulk of network is given a AS Number.
    - So, when one bulk wants to connect with another, BGP identifies it through AS Number.
    - Each AS has a IP Space, which defines what IP Address those AS controls.
    - I believe, this is why Jhaddix wants to identify the ASN of each host, so that we know what IP Space that company withstands.
    
# What is Concurrent requests and Threads?
     - Concurrent requests are requests that are send to application. If we set concurrent requests to 5 then 5 parallel requests will be send to application.
     - Now, in this case, threads come into picture, lets say we send 5 requests, however default value of thread is set to 1, then only one request will be processed whereas if we set threads to 10, then 2 threads will process each request, and application will run faster.
     - We need to tweak these 2 parameters and check what's best for us.
    
# OAUTH
- Oauth is used for authorization of particular resource and not authentication.

# HTTP
- Lets check some response codes
    - 100-199 -> These are ?
    - 200-299 -> Good response, everything is correct and can access the resource.
    - 300-399 -> Redirect response, whenever you visit that page, and you might get either temporary redirect or permanent redirect then these might be response coded you recieve.
    - 400-499 -> These are error response codes, like authorization error, authentication error, page not found error.
    - 500-599 -> Server error, Internal services error, not client fault, its because of services.

# Web Server Softwares
- Web servers softwares are those who manages resources, and provide them to the client when requested.
- Some of common webserver softwares are Apache, Nginx, IIS, Nodejs.
- When client request certain resource, these software provide them from their root directory, for eg: Apache and Nginx has root directory like this /var/www/html/
- Now particular webserver might host multiple domains, so they use virtual hosts to provide particular domain.
- Virtual hosts is just a configuration file on server, if the request header host matches the domain in the file, webserver will provide resources otherwise not.

# Basic Components of Web
- Load Balancer
    - It is attached in between servers and client, and as the name suggest, whenever traffic is high, it will balance out requests on each webserver.
    - Normally, It will check which webserver is currently has lowest number of requests and send the request to that server.
    - Load Balancer also performs health checks, that is, each webserver is responding or not. If particular webserver does not respond, then no traffic will be sent.

- CDN
    - Content Delivery Network(CDN). This also acts as load balancer, lets say particular host has lots of static files. Then CDN will provide those host files from nearest servers located around you, so as to deny traffic.

- WAF
    - Web Application Firewall(WAF).

# HTTP Headers
- <i>This cannot be learned like lets learn all headers at once, not possible and confusing, its better to do it like, during Proxing your request, if you see all those headers then learn those...always better option</i>

# SOP
- Same Origin Policy allows browser to load resource from current domain(tab) only.
- Lets say you are visiting some malicious website and also trusted website(bank), if SOP was not there, then malicious website will make a GET request to bank website, and if SOP is not there, then browser will include bank session cookies into your request and BOOM you get the data.
- BUTTT because of SOP we are only allowed to load or get resources from current domain only.
- Sometimes we want to load resources from different domains or maybe subdomains, thats where RELAXATION plays big role.
- There are different ways to perform relaxation, SINCE sop does not limit JS code, and we can load JS Code from any origin.
- CORS Policy is where relaxation can take place, it tells browser from where all we can load resources.
    Access-Control-Allow-Origin: https://*.example.com
- This will load resources from any subdomains.

# CSP
- Content Security Policy(CSP) Header is used for security purpose to tell browser from where we should load resources using Policy.
- So for example, scripts should only be loaded from current domain and it should not be loaded from any random domain. This can be achieved by specifying this value: script-src: self This is policy(script-src: self)
- If lets say you want to load other resources, like all other default resources from different domains, example, load fonts from fontawsm or load from googleanalytics and many more... we can use tags like fonts-src: example.com
- Now lets say some policy are not defined and you want to load those resources, then we can do default-src: example.com
- This prevents attacker from loading scripts from external domains, also CSP will block inline scripts and HTML Entities.
- Now we can also use one csp header to report all violations that are performed.
    Content-Security-Policy-Report-Only:
        script-src: self;
        default-src: self;
        report-usi: https://www.example.com/csp_violations/
    - This will report all violations that are performed, and we can use only this header if we don't want to use CSP.

# Just some random keyboard shortcuts
alt + tab -> to switch between windows, press alt + tab then release tab and switch between windows with tab key.


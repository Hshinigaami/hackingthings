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

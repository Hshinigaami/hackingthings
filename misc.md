# Index

- [Reverse Proxy](#Reverse-Proxy)
- [Defensive Security](#Defensive-Security)
- [Principles of Security](#Security-Principles)

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


# Methodologies

# Enumeration
	1. NMAP
		a. nmap -sC -sV -oA picklerick IP_ADDRESS
		b. sC - default scripts, sV - enumerate versions, oA - Output in all format

	2. Directory Brute Forcing
		a. FFUF
			1. ffuf -w WORD_LIST -u URL -fc 404
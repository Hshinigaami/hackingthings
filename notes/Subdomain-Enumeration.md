## OSINT Enumeration
- Lets start with Certificates.
    - When host needs to communicate securely, they need TLS/SSL certificates assigned by CA(Certificate Authority)
    - This certificate logs are publicily accessible in site https://crt.sh/ and https://transparencyreport.google.com/https/certificates
    - Subdomains are part of DNS(Layer 7), they will be mapped to pair of DNS Servers with COA(Certificate of Authority) and NS(Name Server) Records.

- Search Engines
    - Google
        ```site:*tryhackme.com```

- Tools
    - dnsrecon
        - This tool will send 1000's of requests to site with wordlist provided to search for subdomain.
        - ```dnsrecon -t brt -d domainname```
        - t is type where brt is Brute Force
    
    - sublist3r
        - ```sublist3r -d domainname -t 50 -b -p 80,443,21,22 -e google,yahoo,baidu```
        - -t no of threads, -b bruteforce, -p ports, -e searchengines
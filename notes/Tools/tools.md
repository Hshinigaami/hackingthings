# Tools

# Hydra

## How to use Hydra on HTTP Auth Method(Which u would call popup authentication)
- ```Hydra -l <USER> -P <PASSWORD_FILE> -s 8080 -f 10.14.79.90 http-get /protected```

    - -s is port no, -f is to stop Hydra if one password matches.

# FFUF

## Directory Fuzzing
- ```ffuf -w wordlists -u url/FUZZ/```
    - FUZZ parameter is where each word will be supplied.

## How to fuzz in signup page
- ```ffuf -w wordlist -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u url -mr "username exists"```
    - -w is wordlist, -X method, -d data, -H Header, -u url, -mr Filter this error

## How to fuzz in login page with two FUZZING parameters or two wordlists.
- ```ffuf -w usernamelist:W1,passwordlist:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u url -fc 200```
    - Here Each value of W1 is checked with all values of W2. So total possibilites should be W1xW2
    - :W1 is first wordlist, :W2 is second wordlist, -fc is filter this status code


# DIRBUSTER

# DIRB

# SUBLIST3R

## Subdomain Enumeration
- sublist3r
        - ```sublist3r -d domainname```

# CURL

## How to list request and response headers i.e verbose information
- ```curl -v attacker.com```

# WGET

# HTTPX

# DNSX

# SUBFINDER

# DNSRECON

## How to bruteforce subdomains by sending multiple requests.
- ```dnsrecon -t brt -d domainname```
        - t is type where brt is Brute Force

# Metasploit

# Burp Suite

# SQLMAP

# BEeF

# Manage_tools (CTF) - https://github.com/zardus/ctf-tools
- ```manage-tools list```

# pwn_tools (CTF)
- Python package for developing exploit code.
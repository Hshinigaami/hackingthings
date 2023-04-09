# Social Tips and Tricks

# Commands
1. My way to get IPs with ports on subdomain list ☪️🛡️

subfinder -d <URL> -silent | dnsx -a -ro -silent | sort -u | naabu -silent | tee ips.txt

2. Someone asked me how to pass JSON data in SQLMAP, here is what I used:

sqlmap -u 'https://lnkd.in/d4TY3Cke' --data '{"User":"abcdefg","Pwd":"Abc@123"}' --random-agent --ignore-code=403 --dbs --hex

--ignore-code=403 ==> Bypass HTTP 403 Forbidden



# Payloads

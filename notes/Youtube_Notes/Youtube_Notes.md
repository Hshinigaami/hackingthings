# Youtube Notes

## Tommy DeVoss shares his favorite tool
- Mostly manual hacking uses Repeater, Intruder or Turbo intruder.
- Talks about James Kettle
- Tool: XSS Crappy : This python tool will scrap the hidden parameters
- Tool: aquatone : subdomain discovering
- Tool: nmap : Port scanning
- Writes python scripts with friends to do various tasks


##################################################################################




## Bug Hunter's Methodology v4.0 - Recon Edition by Jhaddix
    1. Project Tracking
        - Tools: XMIND, Excel, Vim, Notepad++
        - A tool and method to track your project.
        - Uses XMIND to track the hunt, with root as Project (Tesla) and then subnodes like Recon, Root domains, etc.
        - Under recon some of the subnodes that he keep tracks of are ASN's, Acquistions, Linked Discovery, Reverse WHOIS.
        - Above is just the base, you expand from this base.
        - Now, each root domains can be expanded into it's findings. For ex: tesla.com one of the root domain when expanded has following subnodes: Notes, Interesting Endpoints, Narrow Recon.
    2. Wide Recon
        - Finding as many assets as possible for the given company.
    3. Understand the company
        - Acquistions(Crunchbase)
            1. Search for acquistion of company on crunchbase
            2. Google, if the acquired companies are still tagged to parent company and if we can hunt on them.
        - ASN Enumeration
            1. bgp.he.net
                a. A website where we can search a company's name and it will pop there AS Numbers.
                b. These ASN will tell us the IP Space of the company, once the company has a large network they are assigned with ASN.
                c. Although, this is not a clear picture since there might be some different cloud assets that could exists in the space.
            2. Through Command line
                a. Metabigor is a tool that will fetch asn from bgp and asnlookup.com
                b. ASNLookup is a tool that will fetch from maxmind dataset
                c. These automation is kinda risky since you might enter a company in the tool, however another company with same name in there domain might pop up.
                d. So, normally jasson tries manual bgp flow before automation.
        - ASN Enumeration with AMASS
            1. Now we start looking for more Seed domains of target which company might own.
            2. These are found using ASN where Amass will scan the IP Space that are alloacted to ASN.
        - Reverse whois lookup
            1. We can search for mail, domains registered from orgnaization name using Reverse whois.
            2. http://api.whoxy.com/?key=API_Key&reverse=whois&name=Twitch+Hostmaster
            3. Sometimes, even though company has registered a domain does not mean that it is inscope.
            4. Domlink is a tool that will help us to automate the reverse whois lookup using API_KEY, try to search for a tool that is suitable for you.
        - Ad/Analytics Relationships
            1. Builtwith is a tool that is used to find the relationship of a target.
            2. This tool will give us the Google analytics or new relics code, and if we look at other domains who has the same code they might be related to target.
        - Google Fu
            1. Google dorking, try to find subdomains using dorks.
            2. Few dorks he listed were, copyright text, terms of service text and privacy policy text.
        - Shodan
            1. Another tool to find details about target and get lot of information about there infrastructure.
    4. Enumerating Subdomains
        - Linked Discovery
            1. When you visit your target, there are many links that are embedded on your site, so what jasson does is, he selects all the URL's that burp has scanned so far after you just visit the application and again spider those URL's.
            2. So basically, you try to find more directories and subdomains that are linked in those URL's.
            3. These can be acheived using other two cmd tools as well, like Gospider and Hakrawler.
        - Another tool to find subdomains is Subdomanizer. This will look for subdomains inside javascript files and also some cloud links.
        - One of the same tool is subscrapper, however this will not look for sensitive items that subdomanizer does. For ex; this tool will not look for API_KEYs
    5. Subdomain scrapping
        - Some of the scrapping sources: Censys, Robtex, Waybackmachine, dnsdumpster, netcraft, ptrarchive.com, dnsdbsearch, passive total
        - Some cmd tools that Jasson recommends is Amass and Subfinder for finding subdomains.
        - Github Enumeration: github-subdomains.py is another tool that scrapes subdomains from github. You need to give your PAT of github and it will start scraping.
        - Github has rate limit feature, so jason will run the script 4-5 Times with a delay of 6-10 sec between each run.
        - Shodan Enumeration; shosubgo is a tool that will scrap subdomains from shodan.
        - Some high tier hunters scrap the SSL Certs from all cloud IP Space, for ex; from AWS, Azure they will check the SSL Certs from this cloud services providers, and parse the certificates according to the target.
        - Check Daehee park's blog and Sam Erik talk on defcon for cloud ranges tools.
    6. Subdomain Brute forcing.
        - After we found the subdomains, we can bruteforce the target to find hidden subdomains, However we will need some resolvers in order to be faster.
        - Tools such as Amass and shuffledns will give you good output.
        - With good resolvers we also need good wordlist. Some user uses Tailored Wordlist(Like sorted ones) whereas some uses Massive Wordlist.
        - Check jasson's all.txt wordlist good for brute force, also check Tomnomnom's talk on wordlist creation.
        - Also, you can build your own wordlist from keywords that are present on site itself. Some tools are there, search for them.
    7. Alteration scanning
        - This is just permutation and combination of words in subdomains to find the target.
        - For ex; you can try dev1.target.com, dev2, dev3... Just try to tweak some characters, strings to find and bypass valid subdomains.
    8. Port analysis
        - After we have identified subdomains, we need to port analysis which ports are open on target. Some tools are present like nmap, masscan however, jasson recommends to use masscan because this tool will not do any script processing or network scanning. It will just output port details.
        - Since masscan works on only IP Address, we can use another tool which is dnmasscan, where we supply domain name and it will resolve IP Address for us and feed the IP details to masscan to get the results.
        - Service Scanning: After we have Identified the ports from masscan or dnmasscan we can fetch those to nmap to get the service details.
        - What jason has did is, he got the oG file from NMAP and feed that to brutespray Tool to get the service scanned. This tool will try default authentication methods like default creds and check if those work.
    9. Github Dorking
        - Another useful technique to find information about target is github dorking, where companies might push some sensitive data on github, even though they might have deleted those, it still might exist in commits.
        - Jasson has a script on his github, which performs github dorking.
        - Another tool which is mentioned above, github- search will also fetch good information.
        - Checkout the talk by thegentelman's on Github and Sensitive data exposure.
        - Manually, this can be done in parallel to subdomain enumeration which can take long time.
    10. Screenshotting
        - In this step, we can screenshot all the subdomains which are found.
        - Tools: aquatone, eyewitness, httpscreenshot (Find one that is suitable to you)
    11. Subdomain takeover
        - Checkout edoverflow's github on where he explain how subdomains can be owned. Basically some subdomains of a target are pointed to cloud services for ex heroku or aws, however, when companies found there services are no longer required they remove them. But there CNAME is still tagged to these services, so we can host a bucket on heroku or aws and point to those CNAME's to takeover the subdomain.
        - The above explanation is very vague, I haven't explored too deep in these topic yet, so will update later.
        - Another tools are nuclei and one more not able to remember.
    12. Automation++







##################################################################################





## How to Use Amass Efficiently by @jeff_foley
1. Amass is a tool for mapping the attack surface.
2. Since amass is a recursive tool, it will take time to get the results, if you want to get the output in certain amount of time use Timeout flag.
3. Amass output directory files are located in $HOME/.config/amass , if we don't specify the output directory when using amass command this will output in above directory.
4. If we want the local database which is in above directory, you can use -nolocaldb flag. This can speed up amass
5. Finding subdomains from different sources
    - amass enum -src -ip -d host.com
6. Lets say after some days you arrive and you want to know the summary of your subdomain enumeration, it can be loaded using below command. However, if you set the flag of nolocaldb then it won't work because there is no saved data.
    - amass db -summary -d host.com
7. To get the names or what subdomains were discovered earlier we can use below command
    - amass db -names -d host.com
8. Lets say you want to get the information only from certain data sources you can use -include flag.
    - amass enum -src -include crtsh,radb -d host.com
    - This will output from crtsh and radb database.
    - we can use passive flag in order to get faster results but this time, you would miss some infrastructure.
9. When we want to do subdomain bruteforce, we can use -brute option, by default it is set to 1 which means only l1.example.com will return however a1.l1.example.com won't be discovered. We can set it to 2 or 3 in config file.
    - amass enum -brute -d host.com
10. How can we get amass to work faster, it depends upon the number of resolver it has, default is 8. We can add more resolvers
    - Using a resolver list can be or cannot be effective, since we don't know where this resolver exist so they might end up giving us false or malicious results.
    - He used DNSValidator for getting the resolver list.
    - Now he does not use all 9000 dns resolvers and send it to amass, 25-50 at a time is sufficient.
        - sort -R 9000resolvers | tail -n 25 > 25resolvers.txt
        - amass enum -rf 25resolvers.txt -max-dns-queries 20000
    - In above command you would see, we used -max-dns-queries options, that's because even though we give them 25resolvers, the option is set to default to run dns-queries according to default resolvers. So we need to give this option to work faster.

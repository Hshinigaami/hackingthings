## Manual Discovery
- robots.txt file. This file contains list of contents that search engines are restricted to crawl. It won't appear if we google search content listed in the file.

- sitemap.xml file. This file tells webcrawlers to intentionally crawl through this resources. Sometimes, if site is big enough or resources are not linked to each other, this file helps a lot. <b>It can also contain all resouces, that you might have missed to target.</b>

- http-headers (```curl -v attacker.com```) It can show us many good parameters. Such as version, stack and many different things.

## OSINT
- Google DORK - This is best, list will be getting updated in future. - https://en.wikipedia.org/wiki/Google_hacking
    - ```site:``` This will only search for particular site
    - ```intitle:``` 
    - ```inurl:```
    - ```filetype:```

- Wappalyzer - This is extension that will tell us what type of technologies are used for the website with version.

- https://archive.org/web/ - This will give us previous versions of website, if snapshot is taken.

- Use github to search for company repo, sometimes it is used as source control.

- If there are static files that company wants to host then, they can use amazon s3 buckets.
    - This buckets end with - http(s)://{name}.s3.amazonaws.com
    - Normally naming convention for this buckets are found in opensource or need to discover.
    - We can use wordlists to discover name, for example companyname-```FUZZ```.s3.amazonaws.com so fuzz parameter can be assets, private, public, www
    - Eg: https://tryhackme-assets.s3.amazonaws.com/ 
    - <i> Do some more research </i>

## Automated
- This is done by using tools like ffuf, dirbuster, gobuster
    - ```ffuf -w wordlists -u url/FUZZ/```
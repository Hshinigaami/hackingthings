## OAUTH
- Oauth is used for authorization of particular resource and not authentication.

## HTTP
- Lets check some response codes
    - 100-199 -> These are ?
    - 200-299 -> Good response, everything is correct and can access the resource.
    - 300-399 -> Redirect response, whenever you visit that page, and you might get either temporary redirect or permanent redirect then these might be response coded you recieve.
    - 400-499 -> These are error response codes, like authorization error, authentication error, page not found error.
    - 500-599 -> Server error, Internal services error, not client fault, its because of services.

## Web Server Softwares
- Web servers softwares are those who manages resources, and provide them to the client when requested.
- Some of common webserver softwares are Apache, Nginx, IIS, Nodejs.
- When client request certain resource, these software provide them from their root directory, for eg: Apache and Nginx has root directory like this /var/www/html/
- Now particular webserver might host multiple domains, so they use virtual hosts to provide particular domain.
- Virtual hosts is just a configuration file on server, if the request header host matches the domain in the file, webserver will provide resources otherwise not.

## Basic Components of Web
- Load Balancer
    - It is attached in between servers and client, and as the name suggest, whenever traffic is high, it will balance out requests on each webserver.
    - Normally, It will check which webserver is currently has lowest number of requests and send the request to that server.
    - Load Balancer also performs health checks, that is, each webserver is responding or not. If particular webserver does not respond, then no traffic will be sent.

- CDN
    - Content Delivery Network(CDN). This also acts as load balancer, lets say particular host has lots of static files. Then CDN will provide those host files from nearest servers located around you, so as to deny traffic.

- WAF
    - Web Application Firewall(WAF).

## HTTP Headers
- <i>This cannot be learned like lets learn all headers at once, not possible and confusing, its better to do it like, during Proxing your request, if you see all those headers then learn those...always better option</i>

## SOP
- Same Origin Policy allows browser to load resource from current domain(tab) only.
- Lets say you are visiting some malicious website and also trusted website(bank), if SOP was not there, then malicious website will make a GET request to bank website, and if SOP is not there, then browser will include bank session cookies into your request and BOOM you get the data.
- BUTTT because of SOP we are only allowed to load or get resources from current domain only.
- Sometimes we want to load resources from different domains or maybe subdomains, thats where RELAXATION plays big role.
- There are different ways to perform relaxation, SINCE sop does not limit JS code, and we can load JS Code from any origin.
- CORS Policy is where relaxation can take place, it tells browser from where all we can load resources.
    Access-Control-Allow-Origin: https://*.example.com
- This will load resources from any subdomains.

## CSP
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

## Just some random keyboard shortcuts
alt + tab -> to switch between windows, press alt + tab then release tab and switch between windows with tab key.


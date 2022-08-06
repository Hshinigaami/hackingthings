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
    - Web Application Firewall(WAF). I


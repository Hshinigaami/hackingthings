# Index

- [Reverse Proxy](#Reverse-Proxy)

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
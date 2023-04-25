## What is Broken Authentication
- Broken authentication refers to session management and credential management.
- Session Hijacking and Stolen login creds are few mechanism of BAC
- Session ID's normally come in cookies or URL's(Not recommended)
- Few things application should consider for session management
    - How long does session last?
    - How you issue Session ID to user or revoke the ID?
    - Is Session ID Linked to IP Address?
- Some of the session management attacks.
    - Session Hijacking
    - Session ID URL Rewriting: Basically Individual session ID is placed in URL of a website
    - Session Fixation: In this case, attacker predetermines the session ID of the user.
- Credential Stuffing
    - In this case, stolen creds from one site is used on the other site. This works because people use same passwords on all sites.
- Password Spraying
    - Similar to cred stuff, however, in this scenario, attacker uses common credentials like (123456, Password.. etc) on the site.
    - The lockout mechanism of website can be broken by using one username and one password rather than same username and multiple passwords.
- Phishing Attacks
    - Attackers sends a link to user or company and lures the user to enter there creds on to the site controlled by attacker.
    - Spear phishing means controlling users emotions, for ex: sending a link via subject picture of your sister.

## How to prevent broken authentication
- In session management, don't use same session ID every time, don't use session ID in URL.
- Use multi factor authentication(MFA)
- Don't store passwords in clear text
    - Hash the passwords, attacker won't be able to guess the hashed password, however, if two passwords are same and hash is also same then that's and issue.
    - To prevent this add a extra string onto the password(this is called SALT) and then hash the password.
- 

## Common Way
### Look for valid usernames in Signup page
- Try bruteforcing login page if we have permission to use long attempts.
- ffuf -w wordlist -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u url -mr "username exists"
- After you get list of usernames, go to login page and try bruteforcing with password wordlist.

### Try to Bypass authentication in Login Page
- ffuf -w usernamelist:W1,passwordlist:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u url -fc 200

## Altering Cookies
- Cookies are assigned by server to user which contains session information and log in details, since it can be used next time user logs in they won't have to enter login information.
- Sometimes, we can find cookies in Normal text, which is readable, we can alter those easily(very hard to find)
- Cookies can be in hash format, i.e they are hashed using some techniques/Algorithms, this are irreversible but, website like crackstation.net contains database millions of hashes and there result and we can find there.
- Cookies can be in encoded format like base32 or base64, encoding is altering text to certain text. This are reversible.

## Multifactor authentication
### Notes from - https://www.youtube.com/watch?v=4Y_NQbNQLg8
- What is 2FA?
    - Data breaches that have leaked usernames and passwords, which is why 2FA is every website is necessary.
    - 2FA means second factor authentication, while username and password is first level of authentication, after entering correct password, you will be prompted for second level.
    - Now this can be secret questions, authentication code, or maybe some biometric mechanisms.

# Just some notes

1. Vertical access control => Normal user -> Admin
2. Horizontal access control => Normal user1 -> Normal usser2 details
3. Context-Dependent application control => User1 deleted -> still able to login or edit details
   1) Basically, wrong doing of user details, even after user has made permanent changes to it.
   2) Portswigger example: user made payment but still we are able to edit the shopping cart details, like adding more contents to it.
4. Vertical privelege escallation
   1) No protection over sensitive functionality
   2) Normal user can access the admin function through url
5. X-Original-Url or X-Rewrite-Url
   1) With this header set, if we are fetching for / this page, but because of the header, application might return us /admin resource.\
   2) These are custom headers in some of the PHP Frameworks
   3) 

# Tips and tricks 😁

- POST /account/teamsetting/retired_team?team_id=victim’s_id%20
    - In ID parameter, if ID does not work add, %20 in the end and send the request
    - We can even use some special characters (/) or encoded string values.
    - Don't give up just because you got unauthorised access.
- Parameter Pollution
    - GET /api/card?custom_id=<attacker_id>&custom_id=<victm's_is>
- Change request methods.
- Add custom parameter to each request.
    - For eg, /add/card endpoint add parameter like /add/card?custom_id=victimid

## **XSS Rat Tips**

1. Accessing file/events of another user.
2. What if trial account cannot execute all functionality, try executing those.
3. Following conditions
    1. Different Users
    2. Different users with different priveleges
    3. Functions/Events which are not accessible by low privelege users
4. JS Files contains some functions that can be executable
    1. Devs might disable UI Elements, but JS Functions might be still executable
    2. Eg: Invoice button might be disabled, but if you go to JS File and execute that function which will print all Invoice details...IDOR+sde
5. Intellisense - If we write letter a it will search for all javascript functions from all js files of page which contains letter a.
6. Watch TOMNOMNOM video regarding Developer console + JS
7. Login as High Priv get the link which is not accessible by low priv users, Logout and then try to access that link or functionality as low priv users.
8. High Priv users actions/Functionality send them to Repeater then replace the Authorization cookies with low priv users, if we are able to access it...IDOR
9. Use burp's Authorise and Autorepeater plugin.
10. Cookies are of low priv users but if we replace sessions from low priv users to high priv users?? What could happen?

# Methodologies

*While testing for BAC do this*

1. Explore Target
2. Create users of all privelege levels
3. Make a mindmap
4. Hack
5. Report

1. going through /admin function, with normal user
2. accessing admin endpoint with url parameter
   1) Can we escalate user privelege through login function? /login?returnUrl=%2f&role=admin or /login?returnUrl=%2f&admin=true
3. Check with different headers
   1) How can we check, if backend application supports X-Original-Header or X-Rewrite-Url
      1- Maybe, by trying... as per zseaon methodology
   2) This one should bypass the restriction: (https://github.com/sting8k/BurpSuite_403Bypasser/issues/4)
        GET / HTTP/1.1
        Host: example.com
        X-Rewrite-URL: /.git/
4. If post request is made to edit settings, try GET Request, that works sometimes.
5. Check for any parameter through which we can access others. like https://0a7100ea030157bac0f6db3800db0019.web-security-academy.net/my-account?id=carlos
   1) If id parameter changed, we get other users.
6. What if ID Parameter is referenced through GUID, try to find this GUID somewhere is webapplication or waybackurl...Or else, try to decode the GUID using guid tool(if version is 1)...check intruder.io website.
7. If after changing id value to victim, we get redirect, check the response, if it contains some sensitive data... This can happen, if there is no call die() function after redirect.
8. After changing ID Parameter, if host still shows normal user, check source code, if something is changed????
9. Sometimes, application stores logs or any sensitive data, and if they are accessed using incrementation of values, then it can lead to sensitive data exposure. 
   1) For eg https://0a3d008003fc675fc0be1fe1006c004a.web-security-academy.net/download-transcript/1.txt if we increment 1.txt to 2.txt ....??? then ohhh


# Some Important functions to check

1. Price manipulation
2. View sensitive information
3. Editing Blogs
4. IDOR to Account takeover
5. Deleting Victim data
6. Publish private blogs/videos through another user account.
7. Changes
   1) Phone number
   2) Email
   3) Password
   4) Account Delete
   5) User Editing Delete Function
   6) Country Add/Delete
   7) User Role change
   8) Admin Account editing
   9) API/Version Change
   10) JWT Change
   11) File Reading/Write Change

# REMEDIATION FOR X-Original-Url and X-Rewrite-Url
1. Log in to the Online Store node using SSH.
2. Modify the 0ssl.conf file:
vim /etc/httpd/conf.d/0ssl.conf
3. Add the following lines to the <VirtualHost *:443> section:
RequestHeader unset X-Original-URL
RequestHeader unset X-Rewrite-URL
4. Save the changes.
5. Restart the httpd service:
service httpd restart

# Reports
1. IDOR to add secondary users in www.paypal.com/businessmanage/users/api/v1/users to PayPal - 679 upvotes, $10500
2. IDOR allow access to payments data of any user to Nord Security - 334 upvotes, $1000
3. idor allows you to delete photos and album from a gallery to Redtube - 265 upvotes, $1500
4. IDOR allows any user to edit others videos to YouPorn - 242 upvotes, $1500
5. Singapore - Account Takeover via IDOR to Starbucks - 218 upvotes, $6000
6. IDOR delete any Tickets on ads.tiktok.com to TikTok - 184 upvotes, $5000
7. I.D.O.R To Order,Book,Buy,reserve On YELP FOR FREE (UNAUTHORIZED USE OF OTHER USER'S CREDIT CARD) to Yelp - 181 upvotes, $2500
8. IDOR when editing users leads to Account Takeover without User Interaction at CrowdSignal to Automattic - 178 upvotes, $650
9. IDOR in the https://market.semrush.com/ to Semrush - 153 upvotes, $5000
10. IDOR leads to Edit Anyone's Blogs / Websites to Automattic - 141 upvotes, $200
11. [api.pandao.ru] IDOR for order delivery address to Mail.ru - 119 upvotes, $3000
12. IDOR vulnerability (Price manipulation) to Acronis - 119 upvotes, $400
13. IDOR in https://3d.cs.money/ to CS Money - 110 upvotes, $200
14. IDOR and statistics leakage in Orders to Twitter - 109 upvotes, $289
15. Getting access of mod logs from any public or restricted subreddit with IDOR vulnerability to Reddit - 105 upvotes, $5000

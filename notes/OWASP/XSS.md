# XSS

Notes

1. Whenever you try any payload for xss.
    1) Check if value is reflected in response.
    2) Check if any special characters are html encoded??

2. What if script or any malicious word is blocked?
    1) There are multiple ways to execute javascript
    2) for eg in case we are allowed to paste link and it is referenced directly in a HREF tag then google</a> this payload can be used.
    3) div tag, img tag, and there are many tags who has javascript events loaded.

3. What if alert is blocked and script is not blocked
    1) convert ascii value of alert and payload to string and paste it in eval, if script is not blocked … very rare.

4. What if, we can escape the js by single quotes and comment?

5. What if, special characters are html encoded?
    1) Here, it is common in php to use htmlentities as encoding function.
    2) But, if we do not set ENT_QUOTES flag…function won’t encode ‘ (single quotes) and we can use it to escape it.

6. Sometimes, developer used and trusted PHP_SELF which is the path provided by the user.
    1) So, this time, if index.php is where response is reflected, try to do something like this -> /index.php/XSS_Payload
    2) Check the source code, if /index.php/1 is reflected in forms tag, then replace 1 with XSS_Payload
    
# Misc

1. If HTTP-only flag is set, client side javascript script cannot access user cookies. It does not mean that cookies are hidden, it's just if XSS Attack is carried out, cookies won't be fetched. 

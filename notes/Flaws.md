# CODE FLAWS
## Lets start with PHP
### Authentication Flaw
```
if(url.substr(0,6) === '/admin'){
    // CHECK FOR AUTHENTICATION
}else{
    // VIEW THE PAGE
}
```

- Now here, if user goes to ```/admin``` page then if loop is true and authentication is checked.
- If user goes to ```/Admin``` page, if loop is not true and else loop will work to view admin page


# LOGIC FLAWS
### RESET PASSWORD FLAW
- Lets say we have reset password page, we enter email and host requests GET request to ```/customer/reset?email=customer@company.com```
- Now host is asking us to enter username to verify if username and email matches(now a days this is not validated, mail is directly sent to mentioned mail id) -- This is POST request
- Backend verifies email id(provided from last get request) and retrieves username.
- Then host will send POST request with username attached, it verifies username and sends mail. <b>but</b>
- What if email id is not verified during post request and same key parameter is used to send mail id.
- This time, we will send ```username=robert&email=attacker.com```
- Now we have shifted from code logic, we have altered email id parameter by supplying them attacker email.
- See, it will work like this, 
```
    if (username retrieved from get request === POST_DATA.username) {
        send_mail(email,username) // But here we will alter email parameter by sending email=POST_DATA.email
    }
```
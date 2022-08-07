## Lets start with PHP
### Authentication Flaw
```
if(url.substr(0,6) === '/admin'){
    // CHECK FOR AUTHENTICATION
}else{
    // VIEW THE PAGE
}
```

- Now here, if user goes to /admin page then if loop is true and authentication is checked.
- If user goes to /Admin page, if loop is not true and else loop will work to view admin page